from pylenium.driver import Pylenium

from jobs import google


def test_scrape_20_jobs_from_google(py: Pylenium):
    jobs = google.scrape(py, google.SOFTWARE_QA_ENGINEER_IN_UTAH)
    assert len(jobs) == 20
