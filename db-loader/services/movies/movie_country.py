from sqlalchemy import MetaData, insert, null
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from db_server import movies_engine, countries_connection 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from db_server import movies_engine, countries_connection 

movies_db_df = pd.read_sql('SELECT movie_id, title FROM movie', con=movies_engine)
countries_db_df = pd.read_sql('SELECT country_id, name FROM country', con=countries_connection)

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'datasets\\clean\\movie.csv'))
print(df.columns)

df = df.merge(movies_db_df, on='title', how='inner')
df = df.merge(countries_db_df, left_on='production_countries', right_on='name', how='inner')

movie_country_df = df[['movie_id', 'country_id']].drop_duplicates()

metadata = MetaData()
metadata.reflect(bind=movies_engine)
movie_country_table = metadata.tables['movie_country']

with movies_engine.begin() as conn:
    stmt = insert(movie_country_table).prefix_with("IGNORE")
    conn.execute(stmt, movie_country_df.to_dict(orient='records'))
    print(f"✅ Inserted {len(movie_country_df)} rows into movie_country (duplicates ignored)")
