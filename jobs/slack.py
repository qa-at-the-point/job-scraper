""" Slack Block Builder Kit: https://app.slack.com/block-kit-builder

This leverages the Slack Incoming Webhook integrations, which uses Slack Blocks to build messages.
"""

from typing import Dict, List

import requests
from requests import Response

from jobs import config
from jobs.models import Job


def header_block(header: str) -> Dict:
    """Create a Header Block with the given header text"""
    return {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": header,
            "emoji": True,
        },
    }


def divider_block() -> Dict:
    """Create a Divider Block"""
    return {"type": "divider"}


def markdown_block(text: str) -> Dict:
    """Create a Markdown Block with the given text"""
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": text,
        },
    }


def start_blocks_payload() -> Dict:
    """Start the Slack Blocks payload that is eventually sent to Slack"""
    return {
        "blocks": [
            markdown_block(
                """
                \n:wave: Hello! Below are this week's open Job Postings that I've gathered.
                \n\n:bug: You can log any issues or requests <https://github.com/qa-at-the-point/job-scraper/issues|here>
                """
            )
        ]
    }


def create_jobs_payload(jobs: List[Job]) -> Dict:
    """Creates the entire Slack Blocks payload for posting to Slack."""
    payload = start_blocks_payload()
    indeed_header = header_block("Remote Jobs from Indeed")
    payload["blocks"].append(indeed_header)
    payload["blocks"].append(divider_block())

    for job in jobs:
        markdown = markdown_block(f"🔸 *<{job.share_link}|{job.title} at {job.company}>*")
        payload["blocks"].append(markdown)
    return payload


def post_to_channel(payload: Dict) -> Response:
    """Post a Slack Blocks payload to the Slack Channel."""
    response = requests.post(config.SLACK_WEBHOOK_URL, json=payload)
    return response
