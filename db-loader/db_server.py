import sys
sys.dont_write_bytecode = True

from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")

# Get the database name from the environment variable
MYSQL_USERS_DB = os.getenv("MYSQL_USERS_DB")
MYSQL_MOVIES_DB = os.getenv("MYSQL_MOVIES_DB")
MYSQL_COUNTRIES_DB = os.getenv("MYSQL_COUNTRIES_DB")
MYSQL_LANGUAGES_DB = os.getenv("MYSQL_LANGUAGES_DB")

#--------------------------------- MAIN DATABASE ---------------------------------#
# USERS database
USERS_DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_USERS_DB}"
users_engine = create_engine(USERS_DATABASE_URL, echo=True)
users_connection = users_engine.connect()

# MOVIES database
MOVIES_DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_MOVIES_DB}"
movies_engine = create_engine(MOVIES_DATABASE_URL, echo=True)
movies_connection = movies_engine.connect()

#--------------------------------- COMMON DATABASE ---------------------------------#
# COUNTRIES database
COUNTRIES_DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_COUNTRIES_DB}"
countries_engine = create_engine(COUNTRIES_DATABASE_URL, echo=True)
countries_connection = countries_engine.connect()

# LANGUAGES database
LANGUAGES_DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_LANGUAGES_DB}"
languages_engine = create_engine(LANGUAGES_DATABASE_URL, echo=True)
languages_connection = languages_engine.connect()