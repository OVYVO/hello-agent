"""Minimal agent template — copy this folder to start a new demo."""

from __future__ import annotations

from hello_agent import OpenAICompatibleClient, load_config, run_agent

from examples.simple_agent.prompt import AGENT_SYSTEM_PROMPT


def echo(text: str) -> str:
    """本地示例工具：原样回显。"""
    return f"echo: {text}"


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
        user_prompt='请调用 echo 工具，参数 text="hello agent"，然后用 Finish 总结结果。',
        tools={"echo": echo},
    )


if __name__ == "__main__":
    main()
