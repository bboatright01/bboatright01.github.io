from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
import os
from database import get_db_engine, get_db_url


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = get_db_url()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
engine = get_db_engine(get_db_url())