from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    DATABASE_URL: str

    class Config:
        env_file = '.env'


BASE_DIR = Path(__file__).resolve().parent
SETTINGS = Settings()
