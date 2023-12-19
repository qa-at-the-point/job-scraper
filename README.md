# QAP's Job Scraper

This job scraper is for the `#jobs` channel in our Slack Community.

## Setup

Prerequisites:

* 🐍 Python 3.10 or higher
* 📦 [Poetry](https://python-poetry.org/) as the package manager
* 👩🏽‍💻 VS Code is the recommended IDE, but you can use others like PyCharm or Sublime

1. Clone the repo and open it in your IDE
2. Open the Intergrated Terminal and install the packages and dependencies

    ```bash
    poetry install
    ```

3. Create a `.env` file with the appropriate ENVIRONMENT_VARIABLES (ask a maintainer)

## Configuration

* Linter and Formatter: [Ruff](https://github.com/astral-sh/ruff#configuration)
* Testing: [pytest](https://docs.pytest.org/)
* Project Config: [pyproject.tom](/pyproject.toml)
