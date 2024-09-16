import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    GITHUB_CLIENT_ID: str = os.getenv('GITHUB_CLIENT_ID')
    GITHUB_CLIENT_SECRET: str = os.getenv('GITHUB_CLIENT_SECRET')

settings = Settings()
