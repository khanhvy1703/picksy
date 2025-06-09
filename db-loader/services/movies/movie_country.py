from sqlalchemy import create_engine, Table, MetaData, insert, text
from sqlalchemy.exc import IntegrityError
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from db_server import movies_engine, languages_connection 

