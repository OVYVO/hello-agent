"""Load LLM settings from environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Config:
    api_key: str
    base_url: str
    model: str


def load_config() -> Config:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "缺少 OPENAI_API_KEY。请复制 .env.example 为 .env 并填入密钥。"
        )

    return Config(
        api_key=api_key,
        base_url=os.getenv("OPENAI_BASE_URL", "https://api.deepseek.com").strip(),
        model=os.getenv("OPENAI_MODEL", "deepseek-v4-pro").strip(),
    )
