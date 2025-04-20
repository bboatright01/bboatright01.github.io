from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()


def get_db_url():
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
    return db_url


def get_db_engine(db_url):
    engine = create_engine(db_url)
    return engine



