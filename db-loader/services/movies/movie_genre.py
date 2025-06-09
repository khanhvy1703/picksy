from sqlalchemy import create_engine, Table, MetaData, insert, text
from sqlalchemy.exc import IntegrityError
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from db_server import movies_engine, genres_connection 

movies_db_df = pd.read_sql('SELECT movie_id, title FROM movie', con=movies_engine)
genres_db_df = pd.read_sql('SELECT genre_id, name FROM genre', con=genres_connection)

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'datasets\\clean\\movie.csv'))
df['genres'] = df['genres'].str.split(', ')
df = df.explode('genres')
df['genres'] = df['genres'].str.strip()

df = df.merge(movies_db_df, on='title', how='inner')
df = df.merge(genres_db_df, left_on='genres', right_on='name', how='inner')

movie_genre_df = df[['movie_id', 'genre_id']].drop_duplicates()

# print(movie_genre_df.head())

metadata = MetaData()
metadata.reflect(bind=movies_engine)
movie_genre_table = metadata.tables['movie_genre']

with movies_engine.begin() as conn:
    stmt = insert(movie_genre_table).prefix_with("IGNORE")
    conn.execute(stmt, movie_genre_df.to_dict(orient='records'))
    print(f"✅ Inserted {len(movie_genre_df)} rows into movie_genre (duplicates ignored)")
