from dotenv import load_dotenv


load_dotenv()

from crew import stock_crew


def run(stock: str = "TESLA"):
    result = stock_crew.kickoff(inputs={"stock": stock})
    return result


def run_cli(stock: str = "TESLA"):
    result = run(stock)
    print(result)


if __name__ == "__main__":
    run_cli("TESLA")
