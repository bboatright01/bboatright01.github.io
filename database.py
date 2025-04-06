from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import mysql.connector


load_dotenv()

db_credentials = os.getenv("DATABASE_CREDENTIALS") # Ensure this is set in your .env file which stores your database connection string

engine = create_engine(db_credentials)
#engine = mysql.connector.connect(db_credentials)

def load_campaigns():
    with engine.connect() as conn:
        result = conn.execute(text("select * FROM campaigns"))
        campaigns = []
        for row in result.all():
            campaigns.append(dict(row._mapping)) # Convert the row to a dictionary
        return campaigns
    
def add_new_campaign(data):
    with engine.connect() as conn:
        result = conn.execute(text("INSERT INTO campaigns (Name, Description, Country, NGO, Funding_Goal) VALUES (:Name, :Description, :Country, :NGO, :Funding_Goal)"), 
            {
                'Name': data['campaign-name'],
                'Description': data['campaign-description'],
                'Country': data['country'],
                'NGO': "WaterWorks International",
                'Funding_Goal': data['funding-goal']
            })
        conn.commit()
        return result
    
def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
