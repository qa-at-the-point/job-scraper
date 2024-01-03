import requests
from requests import Response

from jobs import config


def post_to_channel(message: str) -> Response:
    """Post a message to the Slack Channel."""
    payload = {"text": message}
    response = requests.post(config.SLACK_WEBHOOK_URL, json=payload)
    return response
