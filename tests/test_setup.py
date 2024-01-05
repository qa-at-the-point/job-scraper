from jobs import config


def test_env_vars():
    assert config.OPENAI_API_KEY, "Have you created a .env file with an OPENAI_API_KEY?"
    assert config.SLACK_WEBHOOK_URL, "Have you created a .env file with a SLACK_WEBHOOK_URL?"
