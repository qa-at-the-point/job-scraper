# QAP's Job Scraper

This job scraper is for the `#jobs` channel in our Slack Community.

* [Setup](#setup)
* [High-Level Organization](#high-level-organization)
* [Configuration](#configuration)
* [Scraper](#scraper)

## Setup

Prerequisites:

* 🐍 Python 3.10 or higher
* 📦 [Poetry](https://python-poetry.org/) as the package manager
* 👩🏽‍💻 VS Code is the recommended IDE, but you can use others like PyCharm or Sublime
* ⚙️ `.env` file with SLACK and OPENAI keys (ask maintainer or use your own values)

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

* [main.ipynb](/notebooks/main.ipynb) is the main program that does the scraping and posting to Slack
* `/notebooks` contains notebooks with runnable code!
* `/jobs` contains the core modules for this "product"
* `/tests` contains the tests!
* Config files and such at the Workspace Root

## Configuration

* Linter and Formatter: [Ruff](https://github.com/astral-sh/ruff#configuration)
* Testing: [pytest](https://docs.pytest.org/)
* Project Config: [pyproject.tom](/pyproject.toml)

## Scraper

Currently, this repo scrapes from `Indeed` and `Google Jobs`.

> 💡 I used [this article](https://zety.com/blog/best-job-search-sites) about the "best job sites in 2024" to start

The main steps are:

1. Use [Pylenium](https://docs.pylenium.io) to scrape jobs from Indeed and parse data to a standard format
2. Use AI to filter out irrelevant jobs
3. Post relevant jobs to the `#jobs` channel in the QAP Slack Community
