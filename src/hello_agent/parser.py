"""Parse Thought/Action output from the LLM."""

from __future__ import annotations

import re


def truncate_thought_action(llm_output: str) -> str:
    """只保留第一对 Thought-Action，截断多余内容。"""
    match = re.search(
        r"(Thought:.*?Action:.*?)(?=\n\s*(?:Thought:|Action:|Observation:)|\Z)",
        llm_output,
        re.DOTALL,
    )
    if not match:
        return llm_output

    truncated = match.group(1).strip()
    if truncated != llm_output.strip():
        print("已截断多余的 Thought-Action 对")
    return truncated


def extract_action(llm_output: str) -> str | None:
    """从模型输出中提取 Action 行内容。"""
    action_match = re.search(r"Action: (.*)", llm_output, re.DOTALL)
    if not action_match:
        return None
    return action_match.group(1).strip()


def parse_finish(action_str: str) -> str | None:
    """若 Action 为 Finish[answer]，返回最终答案。"""
    if not action_str.startswith("Finish"):
        return None
    match = re.match(r"Finish\[(.*)\]", action_str)
    if not match:
        return None
    return match.group(1)


def parse_tool_call(action_str: str) -> tuple[str, dict[str, str]]:
    """解析 function_name(arg=\"value\") 形式的工具调用。"""
    tool_name = re.search(r"(\w+)\(", action_str).group(1)
    args_str = re.search(r"\((.*)\)", action_str).group(1)
    kwargs = dict(re.findall(r'(\w+)="([^"]*)"', args_str))
    return tool_name, kwargs
