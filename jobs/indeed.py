from typing import List, Optional

from bs4 import BeautifulSoup
from pydantic import BaseModel
from pylenium.driver import Pylenium


ORIGIN = "https://indeed.com"
REMOTE_QA_ENGINEER = "https://www.indeed.com/jobs?q=Software+QA+Engineer&sc=0kf%3Aattr%28DSQF7%29%3B"


class Job(BaseModel):
    origin: str = ORIGIN
    title: str
    company: str
    location: str
    description: str
    salary: Optional[str]
    remote: Optional[str]
    job_type: Optional[str]
    apply_link: Optional[str]


def parse_job_results(page_source: str) -> List[Job]:
    """Parse the Job Posting Cards from an Indeed Search Results Page.

    Args:
        page_source: The HTML source of the page to parse.
        remote: "Office", "Hybrid", "Remote", or None
    """
    soup = BeautifulSoup(page_source, "html.parser")
    jobs = []

    for job in soup.find_all(attrs={"data-testid": "slider_item"}):
        title = job.find("h2", class_="jobTitle").get_text(strip=True)
        company = job.find("span", attrs={"data-testid": "company-name"}).get_text(strip=True)

        salary_element = job.find("div", attrs={"data-testid": "attribute_snippet_testid"})
        salary = salary_element.get_text(strip=True) if salary_element else None

        location = (
            job.find("div", class_="company_location")
            .find("div", attrs={"data-testid": "text-location"})
            .get_text(strip=True)
        )

        description_elements = job.find("div", class_="job-snippet").find_all("li")
        description = " ".join([elem.get_text(strip=True) for elem in description_elements])

        apply_link_element = job.find("h2", class_="jobTitle").find("a")
        apply_link = apply_link_element["href"] if apply_link_element and apply_link_element.has_attr("href") else None

        job_type_element = job.find(
            "div", attrs={"data-testid": "attribute_snippet_testid"}, text=lambda x: x and "time" in x
        )
        job_type = job_type_element.get_text(strip=True) if job_type_element else None

        jobs.append(
            Job(
                title=title,
                company=company,
                salary=salary,
                job_type=job_type,
                location=location,
                description=description,
                apply_link=f"{ORIGIN}{apply_link}" if apply_link else None,
            )
        )

    return jobs


def scrape(py: Pylenium, search_url: str = REMOTE_QA_ENGINEER) -> List[Job]:
    py.visit(search_url)
    # TODO: Add pagination
    source = py.webdriver.page_source
    jobs = parse_job_results(source)
    return jobs
