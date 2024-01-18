from pylenium.driver import Pylenium

from jobs import indeed


def test_scrape_jobs_from_first_5_pages(py: Pylenium):
    jobs = indeed.scrape(py, indeed.REMOTE_QA_ENGINEER)
    assert len(jobs) == 75, "Did not collect 15 jobs per page for 5 pages"
