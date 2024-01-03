import pytest

from jobs import slack


@pytest.mark.skipif(slack.config.SLACK_WEBHOOK_URL.endswith("cL4oP"), reason="Don't test with public channel")
def test_slack_post_to_channel():
    response = slack.post_to_channel("Hello, World!")
    assert response.ok
