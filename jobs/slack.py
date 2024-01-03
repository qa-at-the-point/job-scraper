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
                "text": ":wave: Hello! Below are today's open Job Postings that I've gathered. There may be missing info or posts that are not relevant.\n\n:bug: You can log any bugs or issues here:\nhttps://github.com/qa-at-the-point/job-scraper/issues",
            },
        },
        {"type": "divider"},
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Jobs",
                "emoji": True,
            },
        },
    ]
}


def create_job_block(job: Job) -> Dict:
    return {
        "type": "section",
        "text": {"type": "mrkdwn", "text": f"*{job.title}*\n\n🏢 {job.company}\n\n📍 {job.location}\n\n💸 {job.salary}"},
        "accessory": {
            "type": "button",
            "text": {"type": "plain_text", "text": "Visit", "emoji": True},
            "value": "click_me_123",  # TODO: Create a dynamic value
            "url": job.apply_link,
            "action_id": "button-action",
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



def post_to_channel(message: str) -> Response:
    """Post a message to the Slack Channel."""
    payload = {"text": message}
    response = requests.post(config.SLACK_WEBHOOK_URL, json=payload)
    return response
