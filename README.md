# QAP's Job Scraper

This job scraper is for the `#jobs` channel in our Slack Community.

## Setup

Prerequisites:

* 🐍 Python 3.10 or higher
* 📦 [Poetry](https://python-poetry.org/) as the package manager
* 👩🏽‍💻 VS Code is the recommended IDE, but you can use others like PyCharm or Sublime
* ⚙️ `.env` file with SLACK and OPENAI keys (ask maintainer)

1. Clone the repo and open it in your IDE
2. Open the Intergrated Terminal and install the packages and dependencies

    ```bash
    poetry install
    ```

3. Create a `.env` file with the appropriate ENVIRONMENT_VARIABLES (ask a maintainer)

    ```bash
    # Run these tests to check if your system is setup
    poetry run pytest tests/test_setup.py
    ```

## High-Level Organization

* [main.py](/main.py) is the main program that does the scraping and posting to Slack
* `/jobs` contains the core modules for this "product"
* `/tests` contains the tests!
* Config files and such at the Workspace Root

## Configuration

* Linter and Formatter: [Ruff](https://github.com/astral-sh/ruff#configuration)
* Testing: [pytest](https://docs.pytest.org/)
* Project Config: [pyproject.tom](/pyproject.toml)
