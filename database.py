from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

db_credentials = os.getenv("DATABASE_CREDENTIALS") # Ensure this is set in your .env file which stores your database connection string

engine = create_engine(db_credentials)

def load_campaigns():
    with engine.connect() as conn:
        result = conn.execute(text("select * FROM campaigns"))
        campaigns = []
        for row in result.all():
            campaigns.append(dict(row._mapping)) # Convert the row to a dictionary
        return campaigns

print(load_campaigns()[0])