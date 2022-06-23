from functools import lru_cache

from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"

def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings