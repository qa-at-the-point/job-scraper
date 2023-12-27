from pylenium.driver import Pylenium
from jobs import indeed


def test_job_extraction(py: Pylenium):
    jobs = indeed.scrape(py, indeed.QA_ENGINEER)
    assert jobs
    assert len(jobs) == 15


def test_pagination(py: Pylenium):
    pass


def test_rank_relevant_jobs():
    pass