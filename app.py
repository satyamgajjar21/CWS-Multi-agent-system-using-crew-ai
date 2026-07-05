from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

from dotenv import load_dotenv


HOST = "127.0.0.1"
PORT = 8000
ROOT = Path(__file__).resolve().parent
INDEX_FILE = ROOT / "index.html"
RUNTIME_HOME = ROOT / ".runtime"


RUNTIME_HOME.mkdir(exist_ok=True)
os.environ["HOME"] = str(RUNTIME_HOME)
os.environ.setdefault("CREWAI_DISABLE_TELEMETRY", "true")
os.environ.setdefault("CREWAI_DISABLE_TRACKING", "true")
os.environ.setdefault("CREWAI_TRACING_ENABLED", "false")
os.environ.setdefault("OTEL_SDK_DISABLED", "true")
load_dotenv()

from main import run


def build_timeline(stock: str) -> list[dict[str, str]]:
    return [
        {
            "title": "Analyst Agent loaded",
            "detail": "Financial Market Analyst is ready with the live stock tool.",
        },
        {
            "title": "Trader Agent loaded",
            "detail": "Strategic Stock Trader is ready to evaluate the analysis.",
        },
        {
            "title": "Live Stock Information Tool called",
            "detail": f"Fetching live market data for {stock}.",
        },
        {
            "title": "Analysis task completed",
            "detail": "The analyst produced the stock performance summary.",
        },
        {
            "title": "Trading recommendation completed",
            "detail": "The trader produced the final Buy, Sell, or Hold decision.",
        },
    ]


def json_response(handler: BaseHTTPRequestHandler, status: int, payload: Any) -> None:
    body = json.dumps(payload, default=str).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


class StockCrewHandler(BaseHTTPRequestHandler):
    def do_HEAD(self) -> None:
        if self.path not in {"/", "/index.html"}:
            self.send_error(404, "Not found")
            return

        body_size = INDEX_FILE.stat().st_size
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(body_size))
        self.end_headers()

    def do_GET(self) -> None:
        if self.path not in {"/", "/index.html"}:
            self.send_error(404, "Not found")
            return

        body = INDEX_FILE.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self) -> None:
        if self.path != "/analyze":
            self.send_error(404, "Not found")
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(content_length)
            payload = json.loads(raw_body.decode("utf-8") or "{}")
            stock = str(payload.get("stock", "")).strip().upper()

            if not stock:
                json_response(self, 400, {"error": "Please enter a stock symbol."})
                return

            result = run(stock)
            json_response(
                self,
                200,
                {
                    "stock": stock,
                    "timeline": build_timeline(stock),
                    "result": str(result),
                },
            )
        except Exception as exc:
            json_response(self, 500, {"error": str(exc)})

    def log_message(self, format: str, *args: Any) -> None:
        return


def serve() -> None:
    server = ThreadingHTTPServer((HOST, PORT), StockCrewHandler)
    print(f"Stock Crew app running at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    serve()
