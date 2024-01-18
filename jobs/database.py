import sqlite3
from pathlib import Path
from typing import Any, List

from jobs.models import GoogleJob, IndeedJob, Job

SQLITE_FILENAME = "database.db"
SQLITE_URL = f"sqlite:///{SQLITE_FILENAME}"


def create(filename: str = SQLITE_FILENAME) -> None:
    """Create a SQLite database with tables to match our jobs.models with the given filename"""
    with sqlite3.connect(filename) as conn:
        c = conn.cursor()

        # Create table for jobs.models.GoogleJob
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS google_jobs (
                id INTEGER PRIMARY KEY,
                origin TEXT NOT NULL DEFAULT 'https://google.com',
                title TEXT,
                company TEXT,
                location TEXT,
                share_link TEXT
            )
        """
        )

        # Create table for jobs.models.IndeedJob
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS indeed_jobs (
                id INTEGER PRIMARY KEY,
                origin TEXT NOT NULL DEFAULT 'https://indeed.com',
                title TEXT,
                company TEXT,
                location TEXT,
                share_link TEXT,
                salary TEXT
            )
        """
        )

        # Create table for relevant jobs after AI filtering
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS relevant_jobs (
                id INTEGER PRIMARY KEY,
                origin TEXT,
                title TEXT,
                company TEXT,
                location TEXT,
                share_link TEXT
            )
        """
        )

        # Commit changes and close the connection
        conn.commit()


def delete(filename: str = SQLITE_FILENAME) -> None:
    """Delete the SQLite database by deleting (aka unlinking) the given .db file"""
    # This can delete any file, so we want to make sure we're deleting a .db file
    if not filename.endswith(".db"):
        raise ValueError(f"Expected a .db filename, got {filename}")
    Path(filename).unlink(missing_ok=True)


def exists(filename: str = SQLITE_FILENAME) -> bool:
    """Check if the SQLite database exists"""
    return Path(filename).exists()


def execute(query: str, filename: str = SQLITE_FILENAME) -> List[Any]:
    """Query the SQLite database and return all rows from the resultset"""
    with sqlite3.connect(filename) as conn:
        c = conn.cursor()
        c.execute(query)
        results = c.fetchall()

    return results


def insert_indeed_jobs(jobs: List[IndeedJob], filename: str = SQLITE_FILENAME) -> None:
    """Insert a list of IndeedJob models into the indeed_jobs table"""
    insert_query = """
        INSERT INTO indeed_jobs (origin, title, company, location, share_link, salary)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    # Prepare the data for insertion
    job_data = [(job.origin, job.title, job.company, job.location, job.share_link, job.salary) for job in jobs]

    with sqlite3.connect(filename) as conn:
        c = conn.cursor()
        c.executemany(insert_query, job_data)
        conn.commit()


def query_indeed_jobs(query: str, filename: str = SQLITE_FILENAME) -> List[Job]:
    """Query the indeed_jobs table and return a list of IndeedJob models.

    The query must have the following SELECT clause to match the IndeedJob model:

        ```
        SELECT * FROM indeed_jobs
        ```
    """
    results = execute(query, filename)
    jobs = [
        IndeedJob(title=row[1], company=row[2], location=row[3], share_link=row[4], salary=row[5]) for row in results
    ]
    return jobs


def insert_google_jobs(jobs: List[GoogleJob], filename: str = SQLITE_FILENAME) -> None:
    """Insert a list of GoogleJob models into the google_jobs table"""
    insert_query = """
        INSERT INTO google_jobs (origin, title, company, location, share_link)
        VALUES (?, ?, ?, ?, ?)
    """

    # Prepare the data for insertion
    job_data = [(job.origin, job.title, job.company, job.location, job.share_link) for job in jobs]

    with sqlite3.connect(filename) as conn:
        c = conn.cursor()
        c.executemany(insert_query, job_data)
        conn.commit()


def query_google_jobs(query: str, filename: str = SQLITE_FILENAME) -> List[GoogleJob]:
    """Query the google_jobs table and return a list of GoogleJob models.

    The query must have the following SELECT clause to match the GoogleJob model:

        ```
        SELECT * FROM google_jobs
        ```
    """
    results = execute(query, filename)
    jobs = [GoogleJob(title=row[1], company=row[2], location=row[3], share_link=row[4]) for row in results]
    return jobs


def query_relevant_jobs(query: str, filename: str = SQLITE_FILENAME) -> List[Job]:
    """Query the relevant_jobs table and return a list of Job models.

    The query must have the following SELECT clause to match the Job model:

        ```
        SELECT * FROM relevant_jobs
        ```
    """
    results = execute(query, filename)
    jobs = [Job(title=row[1], company=row[2], location=row[3], share_link=row[4]) for row in results]
    return jobs


def insert_relevant_jobs(jobs: List[Job], filename: str = SQLITE_FILENAME) -> None:
    """Insert a list of Job models into the relevant_jobs table after AI filtering"""
    insert_query = """
        INSERT INTO relevant_jobs (origin, title, company, location, share_link)
        VALUES (?, ?, ?, ?, ?)
    """

    # Prepare the data for insertion
    job_data = [(job.origin, job.title, job.company, job.location, job.share_link) for job in jobs]

    with sqlite3.connect(filename) as conn:
        c = conn.cursor()
        c.executemany(insert_query, job_data)
        conn.commit()
