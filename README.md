# hello-agent

Agent 学习项目：可复用核心库 + 按功能分目录的演示。

## 目录结构

```
hello-agent/
├── .env.example              # 环境变量模板
├── src/hello_agent/          # 公共核心（LLM / 解析 / ReAct 循环 / 工具）
└── examples/                 # 按功能分文件夹的演示
    ├── travel_agent/         # 旅行助手（天气 + 景点）
    └── simple_agent/         # 最小模板（复制后改即可）
```

## uv 简介

[uv](https://github.com/astral-sh/uv) 是 Astral 出品的 Python 包与项目管理工具。本项目使用 uv 管理依赖。

| 文件              | 作用                                     |
| ----------------- | ---------------------------------------- |
| `pyproject.toml`  | 项目元信息与依赖声明                     |
| `uv.lock`         | 精确版本锁（建议提交到 Git）             |
| `.python-version` | 指定 Python 版本                         |
| `.venv/`          | 本地虚拟环境（已在 `.gitignore` 中忽略） |

## 快速开始

```bash
# 1. 安装依赖
uv sync

# 2. 配置密钥
cp .env.example .env
# 编辑 .env，填入 OPENAI_API_KEY

# 3. 运行某个演示
uv run python -m examples.travel_agent
uv run python -m examples.simple_agent
```

也可直接跑文件：

```bash
uv run python examples/travel_agent/run.py
```

查看核心库帮助：

```bash
uv run hello-agent
```

## 新增演示功能

```bash
cp -r examples/simple_agent examples/my_feature
# 修改 prompt.py / run.py（工具与用户问题）
uv run python -m examples.my_feature
```

## 断点调试（Cursor / VS Code）

1. 打开 `examples/travel_agent/run.py`
2. 在需要处打断点
3. 使用「Python Debugger: Debug Python File」或自建 launch 配置，模块参数设为 `examples.travel_agent`，工作目录为项目根目录

示例 `launch.json` 配置：

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "travel_agent",
      "type": "debugpy",
      "request": "launch",
      "module": "examples.travel_agent",
      "cwd": "${workspaceFolder}",
      "envFile": "${workspaceFolder}/.env"
    },
    {
      "name": "simple_agent",
      "type": "debugpy",
      "request": "launch",
      "module": "examples.simple_agent",
      "cwd": "${workspaceFolder}",
      "envFile": "${workspaceFolder}/.env"
    }
  ]
}
```

## 常用 uv 命令

```bash
uv add requests openai
uv add --dev ruff pytest
uv remove requests
uv lock --upgrade
uv sync
uv run pytest
```

## 安装 uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# 或: brew install uv
uv --version
```
