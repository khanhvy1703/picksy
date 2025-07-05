from pydantic import BaseModel
from datetime import date, datetime
from enum import Enum

class TitleTypeEnum(str, Enum):
    movie = "movie"
    tv_show = "tv_show"

class TitleOut(BaseModel):
    title_id: int
    title: str
    original_title: str | None
    type: TitleTypeEnum
    description: str | None
    release_date: date | None
    homepage_url: str | None
    trailer_url: str | None
    image_url: str | None
    overall_rating: float
    total_ratings: int
    total_votes: int
    duration: int | None
    revenue: int | None
    budget: int | None
    adult: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }