from pylenium.driver import Pylenium

from jobs import indeed


def test_job_extraction(py: Pylenium):
    jobs = indeed.scrape(py, indeed.REMOTE_QA_ENGINEER)
    assert len(jobs) == 75


def test_pagination(py: Pylenium):
    pass
