# core/config.py
from pydantic import BaseSettings, PostgresDsn
from functools import lru_cache

class Settings(BaseSettings):

    APP_NAME                : str = "Personal Finance AI"
    OPENAI_API_KEY          : str = "YOUR_KEY_HERE"
    OPENAI_MODEL_NAME       : str = "gpt-4o-mini"
    OPENAI_EMBEDDING_MODEL  : str = "text-embedding-3-small"

    DB_HOST : str = "127.0.0.1"
    DB_USER : str = "user"
    DB_PASS : str = "pass"
    DB_PORT : int = 22
    DB_NAME : str = "test"

    class Config:
        env_file = ".env"
        extra = "ignore"

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
