from sqlalchemy import create_engine, Table, MetaData, insert, null, text
from sqlalchemy.exc import IntegrityError
import pandas as pd
import os
import sys
import pycountry

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from db_server import movies_engine, languages_connection 

movies_db_df = pd.read_sql('SELECT movie_id, title FROM movie', con=movies_engine)
languages_db_df = pd.read_sql('SELECT language_id, name FROM language', con=languages_connection)

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'datasets\\clean\\movie.csv'))
language_codes = df['original_language'].unique()

def get_language_name(code):
    try:
        return pycountry.languages.get(alpha_2=code).name
    except:
        return null

df['language_name'] = df['original_language'].apply(get_language_name)
df = df.merge(movies_db_df, on='title', how='inner')
df = df.merge(languages_db_df, left_on='language_name', right_on='name', how='inner')

movie_language_df = df[['movie_id', 'language_id']].drop_duplicates()

metadata = MetaData()
metadata.reflect(bind=movies_engine)
movie_language_table = metadata.tables['movie_language']

with movies_engine.begin() as conn:
    stmt = insert(movie_language_table).prefix_with("IGNORE")
    conn.execute(stmt, movie_language_df.to_dict(orient='records'))
    print(f"✅ Inserted {len(movie_language_df)} rows into movie_language (duplicates ignored)")