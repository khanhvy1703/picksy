from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from src.mysql import movie_tvshow_sessionLocal
from src.models.title import Title
from src.schemas.title import TitleOut

router = APIRouter()

def get_db():
    db = movie_tvshow_sessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all movies
@router.get("/", response_model=List[TitleOut])
def list_movies(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit
    movies = db.query(Title)\
        .filter(Title.type == "movie")\
        .offset(offset)\
        .limit(limit)\
        .all()
    return movies

# Get movie by ID
@router.get("/{title_id}", response_model=TitleOut)
def get_movie_by_id(title_id: int, db: Session = Depends(get_db)):
    movie = db.query(Title)\
        .filter(Title.title_id == title_id, Title.type == "movie")\
        .first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie