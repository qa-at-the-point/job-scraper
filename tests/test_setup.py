from jobs import config


def test_env_vars():
    assert config.SLACK_WEBHOOK_URL is not None, "Have you created a .env file with a SLACK_WEBHOOK_URL?"
