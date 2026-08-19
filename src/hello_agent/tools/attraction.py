"""Mock attraction recommendation tool."""

from __future__ import annotations

# Mock 景点搜索接口地址（不发起真实网络请求，仅用于演示 Agent 工具调用）
MOCK_ATTRACTION_API = "https://mock-api.local/attractions"

_MOCK_ATTRACTIONS = {
    "北京": [
        ("故宫博物院", "晴天适合户外参观中轴建筑与文物展览"),
        ("颐和园", "天气较好时可沿昆明湖步行或乘船"),
        ("国家博物馆", "阴雨天更适合室内观展"),
        ("南锣鼓巷", "轻便逛街小吃，雨天记得带伞"),
    ],
    "上海": [
        ("外滩", "天气晴朗时适合看江景与夜景"),
        ("上海博物馆", "雨天推荐室内文化游览"),
        ("豫园", "适合短途步行与传统街区体验"),
    ],
}


def get_attraction(city: str, weather: str) -> str:
    """根据城市和天气返回景点推荐（Mock 实现）。"""
    url = f"{MOCK_ATTRACTION_API}?city={city}&weather={weather}"
    print(f"[Mock] GET {url}")

    attractions = _MOCK_ATTRACTIONS.get(city)
    if not attractions:
        return (
            f"根据 Mock 接口 {url} 的返回："
            f"暂未收录「{city}」的景点数据。"
            f"在「{weather}」天气下，建议优先选择室内场馆或城市地标周边短途游览。"
        )

    indoor_keywords = ("雨", "雪", "阴")
    prefer_indoor = any(k in weather for k in indoor_keywords)

    ranked = sorted(
        attractions,
        key=lambda item: ("室内" in item[1] or "馆" in item[0]) is prefer_indoor,
        reverse=True,
    )

    lines = [f"- {name}: {reason}" for name, reason in ranked[:3]]
    return (
        f"根据 Mock 接口 {url} 的返回，"
        f"「{city}」在「{weather}」天气下推荐：\n" + "\n".join(lines)
    )
