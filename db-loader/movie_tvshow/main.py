import logging
import sys
import os
import pandas as pd
from iso639 import languages
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_MOVIE_TVSHOW_DB = os.getenv("MYSQL_MOVIE_TVSHOW_DB")

# Set up the database connection
MOVIE_TVSHOW_DB_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_MOVIE_TVSHOW_DB}"
engine = create_engine(MOVIE_TVSHOW_DB_URL, echo=True)
db_connection = engine.connect()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
movie_path = os.path.join(os.path.dirname(__file__), 'datasets', 'clean', 'movie.csv')
df = pd.read_csv(movie_path)
print(df.columns)

# Genres
unique_genres_set = set()
raw_genres_data = df['genres'].dropna().tolist()
for genre_list in raw_genres_data:
    genres = genre_list.split(",")
    unique_genres_set.update(g.strip() for g in genres if g.strip())
    
# Companies
unique_companies_set = set()
raw_companies_data = df['production_companies'].dropna().tolist()
for company_list in raw_companies_data:
    companies = company_list.split(",")
    unique_companies_set.update(c.strip() for c in companies if c.strip())

# Countries
unique_countries_set = set()
raw_countries_data = df['production_countries'].dropna().tolist()
for country_list in raw_countries_data:
    countries = country_list.split(",")
    unique_countries_set.update(c.strip() for c in countries if c.strip())

# Languages
unique_languages_iso_set = set()
raw_languages_iso_data = df['original_language'].dropna().tolist()
unique_languages_iso_set.update(l.strip() for l in raw_languages_iso_data if l.strip())
language_dict = {}
for code in unique_languages_iso_set:
    try:
        lang = languages.get(part1=code)
        language_dict[code] = lang.name
    except KeyError:
        print(f"Unknown ISO 639-1 language code: {code}")
        language_dict[code] = code

# Movies 
selected_columns = ['title', 'original_title', 'description', 'release_date', 'homepage_url', 'duration', 'revenue', 'budget', 'adult']
selected_df = df[selected_columns]

movies_df = selected_df[[
    'title', 'original_title', 'description', 'release_date',
    'homepage_url', 'duration', 'revenue', 'budget', 'adult'
]].copy()

movies_df = movies_df.where(pd.notnull(movies_df), None)

# Insert into the database
for genre in sorted(unique_genres_set):
    db_connection.execute(text("insert ignore into genres (name) values (:genre)"), {"genre": genre})
print("Genres loaded successfully into the database.")

for company in sorted(unique_companies_set):
    db_connection.execute(text("insert ignore into companies (name) values (:company)"), {"company": company})
print("Companies loaded successfully into the database.")

for country in sorted(unique_countries_set):
    db_connection.execute(text("insert ignore into countries (name) values (:country)"), {"country": country})
print("Countries loaded successfully into the database.")

for iso_code, name in language_dict.items():
    db_connection.execute(text("insert ignore into languages (name, iso_code) values (:name, :code)"), {"name": name, "iso_code": iso_code})
print("Languages loaded successfully into the database.")
    
for _, row in movies_df.iterrows():
    db_connection.execute(text("""
        insert into title (
            title, original_title, description, release_date,
            homepage_url, duration, revenue, budget, adult, type
        ) values (
            :title, :original_title, :description, :release_date,
            :homepage_url, :duration, :revenue, :budget, :adult, :type
        )
    """), {
        "title": row['title'],
        "original_title": row['original_title'],
        "description": row['description'],
        "release_date": row['release_date'],
        "homepage_url": row['homepage_url'],
        "duration": row['duration'],
        "revenue": row['revenue'],
        "budget": row['budget'],
        "adult": row['adult'],
        "type": 'movie' 
    })
print("Movies loaded successfully into the database.")
    
db_connection.commit()