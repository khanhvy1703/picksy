import logging
from sqlalchemy import text
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from db_server import languages_engine

logging.basicConfig(level=logging.INFO)

languages = [
    "Ancient Greek",
    "Arabic",
    "Aramaic",
    "Bengali",
    "Cantonese",
    "Chinese",
    "Classical Chinese",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Gujarati",
    "Hebrew",
    "Hindi",
    "Hokkien",
    "Indonesian",
    "Italian",
    "Japanese",
    "Javanese",
    "Kannada",
    "Korean",
    "Latin",
    "Levantine Arabic",
    "Maghrebi Arabic",
    "Malay",
    "Mandarin",
    "Marathi",
    "Persian (Farsi)",
    "Polish",
    "Portuguese",
    "Punjabi",
    "Russian",
    "Sanskrit",
    "Shanghainese",
    "Spanish",
    "Swahili",
    "Tamil",
    "Telugu",
    "Thai",
    "Turkish",
    "Urdu",
    "Vietnamese"
]

def insert_languages(languages: list):
    query = text("INSERT INTO language (name) VALUES (:name)")
    with languages_engine.begin() as connection:
        for language in languages:
            connection.execute(query, {"name": language})
            
if __name__ == "__main__":
    try:
        insert_languages(languages)
    except Exception as e:
        logging.error(f"An error occurred: {e}")