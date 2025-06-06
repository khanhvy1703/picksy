import logging
from sqlalchemy import text
import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from db_server import movies_connection

logging.basicConfig(level=logging.INFO)
MYSQL_MOVIES_MAIN_TABLE = os.getenv("MYSQL_MOVIES_MAIN_TABLE", 'movies')

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'datasets\\clean\\movie.csv'))

#        'title', 'release_date', 'revenue', 'runtime', 'adult', 'budget',
#        'homepage', 'original_language', 'original_title', 'overview', 'genres',
#        'production_companies', 'production_countries'

df = df.rename(columns={'overview': 'description', 'runtime' : 'duration', 'homepage': 'homepage_url'})

print(df.columns)

selected_columns = ['title', 'original_title', 'description', 'release_date', 'homepage_url', 'duration', 'revenue', 'budget', 'adult']
selected_df = df[selected_columns]

# Make sure these match your MySQL column names
movies_df = selected_df[[
    'title', 'original_title', 'description', 'release_date',
    'homepage_url', 'duration', 'revenue', 'budget', 'adult'
]].copy()

movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')
movies_df = movies_df.dropna(subset=['title'])

# Add to movies database
movies_df.to_sql(name=MYSQL_MOVIES_MAIN_TABLE, con=movies_connection, if_exists='append', index=False, method='multi', chunksize=1000)