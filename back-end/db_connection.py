import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")

DATABASES = {
    "users": os.getenv("MYSQL_USERS_DB"),
    "movies": os.getenv("MYSQL_MOVIES_DB"),
    "countries": os.getenv("MYSQL_COUNTRIES_DB"),
    "languages": os.getenv("MYSQL_LANGUAGES_DB"),
}

def build_db_url(db_name: str) -> str:
    return (
        f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{db_name}"
    )

engines = {
    name: create_engine(build_db_url(db_name), echo=True)
    for name, db_name in DATABASES.items()
}