"""Travel assistant demo: weather + attraction tools."""

from __future__ import annotations

from hello_agent import OpenAICompatibleClient, load_config, run_agent
from hello_agent.tools import get_attraction, get_weather

from examples.travel_agent.prompt import AGENT_SYSTEM_PROMPT


def main() -> None:
    cfg = load_config()
    llm = OpenAICompatibleClient(
        model=cfg.model,
        api_key=cfg.api_key,
        base_url=cfg.base_url,
    )
    run_agent(
        llm=llm,
        system_prompt=AGENT_SYSTEM_PROMPT,
        user_prompt="你好，请帮我查询一下今天北京的天气，然后根据天气推荐一个合适的旅游景点。",
        tools={
            "get_weather": get_weather,
            "get_attraction": get_attraction,
        },
    )


if __name__ == "__main__":
    main()
