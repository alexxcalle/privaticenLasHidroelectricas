from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()