from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.mysql import movie_tvshow_base
from src.models.relationships import title_language

class Language(movie_tvshow_base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, autoincrement=True)  # <-- Fixed column name
    name = Column(String(255), nullable=False)
    iso_code = Column(String(10), nullable=False, unique=True)

    titles = relationship(
        "Title",
        secondary=title_language,
        back_populates="languages"
    )