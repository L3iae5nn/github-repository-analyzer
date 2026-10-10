# GitHub Repository Analyzer

A Python command-line tool for retrieving and analyzing GitHub users' public repositories using the GitHub REST API.
一个基于 Python 和 GitHub REST API 的命令行工具，用于获取和分析 GitHub 用户的公开仓库。

## Features / 功能

- **Repository Retrieval / 仓库获取**
  - Retrieve all public repositories of a specified GitHub user.
  - 获取指定 GitHub 用户的所有公开仓库，支持自动分页。

- **Repository Statistics / 仓库统计**
  - Display the total number of public repositories.
  - 显示用户拥有的公开仓库总数。

- **Top Repositories / 热门仓库排名**
  - Display the five most-starred repositories by default.
  - 默认显示 Star 数量最多的五个仓库，支持自定义数量。

- **Language Statistics / 编程语言统计**
  - Count repositories by their primary programming language and sort the results in descending order.
  - 根据每个仓库的主要编程语言统计仓库数量，并按照数量降序排列。

- **CSV Export / CSV 导出**
  - Export repository names, star counts, and primary programming languages to a CSV file.
  - 将仓库名称、Star 数量和主要编程语言导出为 CSV 文件。

- **GitHub Authentication / GitHub 身份认证**
  - Support optional GitHub Personal Access Token authentication to increase API rate limits.
  - 支持通过 GitHub Personal Access Token 进行身份认证，提高 API 请求额度。

## Installation / 安装

### 1. Clone the repository / 克隆仓库

```bash
git clone git@github.com:L3iae5nn/github-repository-analyzer.git
```

### 2. Navigate to the project directory / 进入项目目录

```bash
cd github-repository-analyzer
```

### 3. Install dependencies / 安装依赖

Make sure Python is installed, then run:
确保已经安装 Python，然后执行：

```bash
python -m pip install -r requirements.txt
```

## Usage / 使用方法

Run the program:
运行程序：

```bash
python project.py
```

Enter the GitHub username you want to analyze.
输入需要查询的 GitHub 用户名。

### Example Output / 输出示例

```text
Github username: example_user

Total repositories: 12

Top 5 Repositories:
1. repository-a - 150 stars
2. repository-b - 100 stars
3. repository-c - 75 stars
4. repository-d - 50 stars
5. repository-e - 25 stars

Language Statistics:
Python: 5 repositories
JavaScript: 3 repositories
C: 2 repositories
Java: 2 repositories

Repositories exported to repositories.csv
```

The program automatically exports all retrieved repositories to `repositories.csv`.
程序运行后，会自动将获取到的所有仓库信息保存到 `repositories.csv`。

The CSV file contains the following columns:

CSV 文件包含以下字段：

| Column / 字段 | Description / 说明 |
|---|---|
| `name` | Repository name / 仓库名称 |
| `stars` | Number of stars / Star 数量 |
| `language` | Primary programming language / 主要编程语言 |

## Configuration / 配置

### GitHub Token / GitHub 身份认证

GitHub limits the number of unauthenticated API requests.
GitHub 对未认证的 API 请求设有频率限制。

To increase the rate limit, create a GitHub Personal Access Token and set it as an environment variable.
如需提高请求额度，可以创建 GitHub Personal Access Token，并将其设置为环境变量。

On macOS or Linux:
在 macOS 或 Linux 终端中：

```bash
export GITHUB_TOKEN="your_github_token"
```

The program reads the token using:
程序通过以下代码读取 Token：

```python
token = os.getenv("GITHUB_TOKEN")
```

Authentication is optional. Without a token, the program can still retrieve public repositories, subject to GitHub's unauthenticated API rate limits.
Token 并非必需。未配置 Token 时，程序仍可获取公开仓库，但会受到 GitHub 未认证请求的频率限制。

**Security Note / 安全提醒：**

Never hardcode your GitHub Token in source code or commit it to a public repository.
不要将真实 Token 直接写入源代码，也不要将其提交到公开的 GitHub 仓库。

### Customizing Output / 自定义输出

The default number of top repositories is five.
默认显示 Star 数量最多的五个仓库。

This can be changed through the `get_top_repos()` function:
可以通过 `get_top_repos()` 函数修改：

```python
top_repos = get_top_repos(all_repos, n=10)
```

The default CSV filename is `repositories.csv`.
默认导出文件名为 `repositories.csv`。

It can be customized through the `export_csv()` function:
可以通过 `export_csv()` 函数自定义：

```python
export_csv(all_repos, filename="my_repositories.csv")
```

These options are configured through function arguments in the Python code, rather than command-line arguments.
这些选项目前需要在 Python 代码中修改函数调用参数，尚不支持通过命令行参数直接配置。

## Testing / 测试

The project uses `pytest` for automated testing.
项目使用 `pytest` 进行自动化测试。

To run the tests:
运行测试：

```bash
python -m pytest test_project.py -v
```

The test suite covers three core functions:
测试覆盖以下三个核心函数：

| Function / 函数 | Purpose / 测试内容 |
|---|---|
| `get_top_repos()` | Repository ranking / 仓库排名 |
| `get_language_stats()` | Language statistics / 编程语言统计 |
| `export_csv()` | CSV file generation / CSV 文件生成 |

The CSV export test uses pytest's `tmp_path` fixture to create temporary files without affecting the actual project output.
CSV 导出测试使用 pytest 提供的 `tmp_path` 创建临时文件，避免影响项目正常生成的 CSV 文件。