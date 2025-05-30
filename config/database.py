from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """mysql db"""
    DB_HOST: str = '127.0.0.1'
    DB_PORT: int = 3306
    DB_DATABASE: str = 'fastapi'
    DB_USER: str = 'root'
    DB_PASSWORD: str = '123456'

    model_config = {
        "extra": "allow",
        "env_file": ".env"
    }


class RedisSettings(BaseSettings):
    """redis"""

    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str] = None

    model_config = {
        "extra": "allow",
        "env_file": ".env"
    }


settings = Settings()
redis_settings = RedisSettings()
