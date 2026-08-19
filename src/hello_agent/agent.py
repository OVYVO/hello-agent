"""ReAct agent loop."""

from __future__ import annotations

from collections.abc import Callable

from hello_agent.llm import OpenAICompatibleClient
from hello_agent.parser import (
    extract_action,
    parse_finish,
    parse_tool_call,
    truncate_thought_action,
)


def run_agent(
    *,
    llm: OpenAICompatibleClient,
    system_prompt: str,
    user_prompt: str,
    tools: dict[str, Callable[..., str]],
    max_steps: int = 5,
) -> str:
    """运行 Thought-Action-Observation 循环，返回最终答案或空字符串。"""
    prompt_history = [f"用户请求: {user_prompt}"]
    print(f"用户输入: {user_prompt}\n" + "=" * 40)

    final_answer = ""
    for i in range(max_steps):
        print(f"--- 循环 {i + 1} ---\n")

        full_prompt = "\n".join(prompt_history)
        llm_output = llm.generate(full_prompt, system_prompt=system_prompt)
        llm_output = truncate_thought_action(llm_output)
        print(f"模型输出:\n{llm_output}\n")
        prompt_history.append(llm_output)

        action_str = extract_action(llm_output)
        if action_str is None:
            observation = (
                "错误: 未能解析到 Action 字段。"
                "请确保你的回复严格遵循 'Thought: ... Action: ...' 的格式。"
            )
            observation_str = f"Observation: {observation}"
            print(f"{observation_str}\n" + "=" * 40)
            prompt_history.append(observation_str)
            continue

        finish_answer = parse_finish(action_str)
        if finish_answer is not None:
            final_answer = finish_answer
            print(f"任务完成，最终答案: {final_answer}")
            break

        tool_name, kwargs = parse_tool_call(action_str)
        if tool_name in tools:
            observation = tools[tool_name](**kwargs)
        else:
            observation = f"错误：未定义的工具 '{tool_name}'"

        observation_str = f"Observation: {observation}"
        print(f"{observation_str}\n" + "=" * 40)
        prompt_history.append(observation_str)

    return final_answer
