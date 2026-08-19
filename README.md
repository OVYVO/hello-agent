# hello-agent

agent 学习

## uv 简介

[uv](https://github.com/astral-sh/uv) 是 Astral 出品的 Python 包与项目管理工具，可统一处理虚拟环境、依赖安装与锁文件。本项目使用 uv 管理依赖。

相关文件：

| 文件              | 作用                                     |
| ----------------- | ---------------------------------------- |
| `pyproject.toml`  | 项目元信息与依赖声明                     |
| `uv.lock`         | 精确版本锁（建议提交到 Git）             |
| `.python-version` | 指定 Python 版本                         |
| `.venv/`          | 本地虚拟环境（已在 `.gitignore` 中忽略） |

## 安装 uv

macOS / Linux：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

或使用 Homebrew：

```bash
brew install uv
```

安装后确认：

```bash
uv --version
```

## 常用命令

### 初始化与同步

```bash
# 在已有目录初始化项目（本仓库已完成，一般无需再执行）
uv init

# 按 pyproject.toml / uv.lock 创建环境并安装依赖
uv sync

# 仅创建虚拟环境
uv venv
```

### 依赖管理

```bash
# 添加运行时依赖
uv add requests openai

# 添加开发依赖
uv add --dev pytest ruff

# 移除依赖
uv remove requests

# 升级锁文件中的依赖
uv lock --upgrade

# 升级后同步到本地环境
uv sync
```

### 运行与环境

```bash
# 在项目环境中运行（推荐，无需手动 activate）
uv run python
uv run python main.py
uv run pytest

# 手动激活虚拟环境（可选）
source .venv/bin/activate
```

### Python 版本

```bash
# 安装指定版本的 Python
uv python install 3.12

# 查看可用 / 已安装的 Python
uv python list
```

### 其他实用命令

```bash
# 查看帮助
uv --help
uv add --help

# 清理缓存
uv cache clean
```

## 快速开始

```bash
# 1. 安装 uv（若尚未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. 进入项目并同步依赖
cd hello-agent
uv sync

# 3. 运行
uv run hello-agent
```
