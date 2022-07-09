import os
from dotenv import load_dotenv
import base64
from pathlib import Path

env_path = Path('.') /'.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME:str = "Simple Portal"
    PROJECT_VERSION:str = "1.0.0"
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD =  base64.b64decode(os.getenv("MYSQL_PASSWORD")).decode("ascii")
    MYSQL_SERVER = os.getenv("MYSQL_SERVER")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_DB = os.getenv("MYSQL_DB")
    DB_URL = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}/{MYSQL_DB}"


settings = Settings()