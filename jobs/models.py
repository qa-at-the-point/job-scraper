from typing import Optional

from pydantic import BaseModel


class Job(BaseModel):
    origin: str
    title: str
    company: str
    location: str
    description: str
    salary: Optional[str]
    job_type: Optional[str]
    apply_link: Optional[str]
