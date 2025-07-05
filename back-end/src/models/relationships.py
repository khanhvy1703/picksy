from sqlalchemy import Table, Column, Integer, ForeignKey
from src.mysql import movie_tvshow_base

title_language = Table(
    "title_language",
    movie_tvshow_base.metadata,
    Column("title_id", Integer, ForeignKey("title.title_id"), primary_key=True),
    Column("language_id", Integer, ForeignKey("languages.id"), primary_key=True)  # <-- Fixed to match `id`
)