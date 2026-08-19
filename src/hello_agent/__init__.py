"""hello-agent: shared core for ReAct-style agent demos."""

from hello_agent.agent import run_agent
from hello_agent.config import Config, load_config
from hello_agent.llm import OpenAICompatibleClient

__all__ = [
    "Config",
    "OpenAICompatibleClient",
    "load_config",
    "run_agent",
]


def main() -> None:
    print(
        "hello-agent 核心库已安装。\n"
        "运行演示：\n"
        "  uv run python -m examples.travel_agent\n"
        "  uv run python -m examples.simple_agent"
    )
