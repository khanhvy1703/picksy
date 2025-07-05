from sqlalchemy import Column, Integer, String, Text, Date, Float, Boolean, Enum, BigInteger, TIMESTAMP
from src.mysql import movie_tvshow_base
import enum

class TitleTypeEnum(str, enum.Enum):
    movie = "movie"
    tv_show = "tv_show"

class Title(movie_tvshow_base):
    __tablename__ = "title"

    title_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(1000), nullable=False)
    original_title = Column(String(1000))
    type = Column(Enum(TitleTypeEnum), nullable=False)
    description = Column(Text)
    release_date = Column(Date)
    homepage_url = Column(Text)
    trailer_url = Column(Text)
    image_url = Column(Text)
    overall_rating = Column(Float, default=0)
    total_ratings = Column(Integer, default=0)
    total_votes = Column(Integer, default=0)
    duration = Column(Integer)
    revenue = Column(BigInteger)
    budget = Column(BigInteger)
    adult = Column(Boolean)
    created_at = Column(TIMESTAMP)