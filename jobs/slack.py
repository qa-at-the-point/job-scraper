""" Slack Block Builder Kit: https://app.slack.com/block-kit-builder """

from typing import Dict, List

import requests
from requests import Response

from jobs import config
from jobs.models import Job


HEADER_BLOCK = {
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":wave: Hello! Below are this week's open Job Postings that I've gathered. There may be missing info since each poster is different.\n\n:bug: You can log any bugs or issues here:\nhttps://github.com/qa-at-the-point/job-scraper/issues",
            },
        },
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Jobs",
                "emoji": True,
            },
        },
        {"type": "divider"},
    ]
}


def create_job_block(job: Job) -> Dict:
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"*<{job.apply_link}|{job.title} at {job.company}>*\n\n📍 {job.location}\n\n💸 {job.salary}",
        },
    }


def create_jobs_payload(jobs: List[Job]) -> Dict:
    """Create a payload for posting to Slack."""
    payload = HEADER_BLOCK
    for job in jobs:
        payload["blocks"].append(create_job_block(job))
        payload["blocks"].append({"type": "divider"})
    return payload


def post_jobs_to_channel(jobs: List[Job]) -> Response:
    """Post a list of jobs to the Slack Channel."""
    payload = create_jobs_payload(jobs)
    response = requests.post(config.SLACK_WEBHOOK_URL, json=payload)
    return response
