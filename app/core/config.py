#  конфигурация всего проекта

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
import os # управлять линукс
from dotenv import load_dotenv # читает env файл и читает из env

load_dotenv()
DB_URL = os.getenv("DB_URL")