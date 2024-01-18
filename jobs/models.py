from typing import Optional

from pydantic import BaseModel


class Job(BaseModel):
    origin: str
    title: str
    company: str
    location: str
    share_link: str


class GoogleJob(Job):
    origin: str = "https://google.com"


class IndeedJob(Job):
    origin: str = "https://indeed.com"
    salary: Optional[str]
