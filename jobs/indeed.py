from typing import List

from bs4 import BeautifulSoup
from pylenium.driver import Pylenium

from jobs.models import IndeedJob

ORIGIN = "https://indeed.com"
REMOTE_QA_ENGINEER = f"{ORIGIN}/jobs?q=Software+QA+Engineer&sc=0kf%3Aattr%28DSQF7%29%3B"


def parse_job_results(page_source: str) -> List[IndeedJob]:
    """Parse the Job Posting Cards from an Indeed Search Results Page.

    Args:
        page_source: The HTML source of the page to parse.
    """
    soup = BeautifulSoup(page_source, "html.parser")
    jobs = []

    for job in soup.find_all(attrs={"data-testid": "slider_item"}):
        header = job.find("h2", class_="jobTitle").find("a")
        title = header.get_text(strip=True)
        share_link = header["href"] if header and header.has_attr("href") else None
        company = job.find("span", attrs={"data-testid": "company-name"}).get_text(strip=True)

        salary_element = job.find("div", attrs={"data-testid": "attribute_snippet_testid"})
        salary = salary_element.get_text(strip=True) if salary_element else None

        location = (
            job.find("div", class_="company_location")
            .find("div", attrs={"data-testid": "text-location"})
            .get_text(strip=True)
        )

        jobs.append(
            IndeedJob(
                title=title,
                company=company,
                salary=salary,
                location=location,
                share_link=f"{ORIGIN}{share_link}" if share_link else None,
            )
        )

    return jobs


def scrape(py: Pylenium, search_url: str = REMOTE_QA_ENGINEER) -> List[IndeedJob]:
    py.visit(search_url)
    pagination = py.find("[aria-label='pagination'] a")
    num_pages = len(pagination) - 1  # Last element is "Next"
    jobs = []

    for i in range(num_pages):
        if i != 0:  # if not on first page, click the next page
            page = py.get(f"[data-testid='pagination-page-{i + 1}']")
            page.click()
        source = py.webdriver.page_source
        jobs.extend(parse_job_results(source))

    # Close the browser
    py.quit()

    return jobs
