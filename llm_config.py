from typing import Any

from crewai import LLM
from crewai.hooks import register_before_llm_call_hook


GROQ_MODEL = "groq/llama-3.3-70b-versatile"


def strip_groq_cache_breakpoints(context: Any) -> None:
    llm = getattr(context, "llm", None)
    model = getattr(llm, "model", "")

    if not isinstance(model, str) or not model.startswith("groq/"):
        return

    for message in context.messages:
        if isinstance(message, dict):
            message.pop("cache_breakpoint", None)


register_before_llm_call_hook(strip_groq_cache_breakpoints)


def create_llm(temperature: float = 0.0) -> LLM:
    return LLM(
        model=GROQ_MODEL,
        temperature=temperature,
    )
