from core.utils.config import config


def test_config():
    key = config.DAYTONA_API_KEY
    print(key)
    api_key = config.OPENAI_COMPATIBLE_API_KEY
    print(api_key)
