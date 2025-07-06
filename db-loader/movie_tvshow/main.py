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

movies_db_df = pd.read_sql('SELECT title_id, title FROM title', con=db_connection)
languages_db_df = pd.read_sql('SELECT id, iso_code FROM languages', con=db_connection)
genre_db_df = pd.read_sql('SELECT id, name FROM genres', con=db_connection)
country_db_df = pd.read_sql('SELECT id, name FROM countries', con=db_connection)
company_db_df = pd.read_sql('SELECT id, name FROM companies', con=db_connection)

df['genres'] = df['genres'].str.split(', ')
df = df.explode('genres')
df['genres'] = df['genres'].str.strip()

df['production_companies'] = df['production_companies'].str.split(', ')
df = df.explode('production_companies')
df['production_companies'] = df['production_companies'].str.strip()

df['production_countries'] = df['production_countries'].str.split(', ')
df = df.explode('production_countries')
df['production_countries'] = df['production_countries'].str.strip()

df = df.merge(movies_db_df, on='title', how='inner')
df = df.merge(languages_db_df, left_on='original_language', right_on='iso_code', how='inner')
df = df.rename(columns={'id': 'language_id'})

df = df.merge(genre_db_df, left_on='genres', right_on='name', how='inner')
df = df.rename(columns={'id': 'genre_id'})

df = df.merge(company_db_df, left_on='production_companies', right_on='name', how='inner')
df = df.rename(columns={'id': 'company_id'})

df = df.merge(country_db_df, left_on='production_countries', right_on='name', how='inner')
df = df.rename(columns={'id': 'country_id'})

movie_language_df = df[['title_id', 'language_id']].drop_duplicates()
movie_genre_df = df[['title_id', 'genre_id']].drop_duplicates()
movie_company_df = df[['title_id', 'company_id']].drop_duplicates()
movie_country_df = df[['title_id', 'country_id']].drop_duplicates()

print(movie_company_df.shape)
print(movie_language_df.shape)
print(movie_genre_df.shape)
print(movie_country_df.shape)

# Insert into relationship tables
movie_language_df.to_sql('title_language', con=db_connection, if_exists='append', index=False)
movie_genre_df.to_sql('title_genre', con=db_connection, if_exists='append', index=False)
movie_company_df.to_sql('title_company', con=db_connection, if_exists='append', index=False)
movie_country_df.to_sql('title_country', con=db_connection, if_exists='append', index=False)

db_connection.commit()

