import logging
from sqlalchemy import text
import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from db_server import movies_connection

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'datasets\\clean\\movie.csv'))
print(df.columns)

selected_columns = ['title', 'original_title', 'description', 'release_date', 'homepage_url', 'duration', 'revenue', 'budget', 'adult']
selected_df = df[selected_columns]

movies_df = selected_df[[
    'title', 'original_title', 'description', 'release_date',
    'homepage_url', 'duration', 'revenue', 'budget', 'adult'
]].copy()

print(movies_df.shape)

try:
    logging.info("Starting to write to SQL")
    movies_df.to_sql(
        name='movie',
        con=movies_connection,
        if_exists='append',
        index=False,
        method='multi',
        chunksize=1000
    )
    logging.info("Finished writing to SQL")
except Exception as e:
    logging.error("Error while writing to SQL: %s", e)
    