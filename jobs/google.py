from typing import List

from pylenium.driver import Keys, Pylenium

from jobs.models import GoogleJob

ORIGIN = "https://google.com"
SOFTWARE_QA_ENGINEER_IN_UTAH = f"{ORIGIN}/search?q=Software+QA+Engineer+jobs+utah"


def parse_job_results(py: Pylenium) -> List[GoogleJob]:
    scraped_jobs = []
    share_search_results_link = None
    results = py.find("[aria-label='Jobs list'] li [role='treeitem']")

    for result in results:
        # 1. Collect its short content
        content = result.text()
        scraped_jobs.append(content)

        if share_search_results_link is None:  # TODO: Get the share_link for each job
            # 2. Click on the Share button within the Details Page
            page = py.get("div#gws-plugins-horizon-jobs__job_details_page")
            page.get("div[aria-label='Share'][role='button']").click(force=True)

            # 3. Find the shareable link
            share = py.find("[aria-label='Share'][role='dialog'] input").last()
            py.wait().until(lambda _: share.get_attribute("value").startswith("https://g.co"))
            share_search_results_link = share.get_attribute("value")

            # 4. Close the dialog
            share.type(Keys.ESCAPE)

    # 5. Parse each Job's content into a GoogleJob object
    parsed_jobs = []
    for job in scraped_jobs:
        job = job.split("\n")
        if len(job[0]) == 1:
            job.pop(0)  # remove the logo character if it has one

        parsed_jobs.append(
            GoogleJob(
                title=job[0],
                company=job[1],
                location=job[2],
                share_link=share_search_results_link
            )
        )

    return parsed_jobs


def scrape(py: Pylenium, search_url: str = SOFTWARE_QA_ENGINEER_IN_UTAH) -> List[GoogleJob]:
    py.visit(search_url)
    py.getx("//a[contains(., 'more jobs')]").click()

    jobs = parse_job_results(py)
    return jobs
