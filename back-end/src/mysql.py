import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_MOVIE_TVSHOW_DB = os.getenv("MYSQL_MOVIE_TVSHOW_DB")

MOVIE_TVSHOW_DB_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_MOVIE_TVSHOW_DB}"
movie_tvshow_engine = create_engine(MOVIE_TVSHOW_DB_URL, echo=True)
movie_tvshow_sessionLocal = sessionmaker(bind=movie_tvshow_engine, autoflush=False, autocommit=False)
movie_tvshow_base = declarative_base()