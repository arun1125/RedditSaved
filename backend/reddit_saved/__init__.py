from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask_cors import CORS
import os
from flask_migrate import Migrate
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://reddit_saved:Nani1125?!@redditsavedinstance.czbffs62tgvp.us-east-2.rds.amazonaws.com/reddit_saved"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://reddit_saved:Nani1125?!@redditsavedinstance.czbffs62tgvp.us-east-2.rds.amazonaws.com:5432/redditsaved'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://reddit_saved:Nani1125?!@redditsavedinstance.czbffs62tgvp.us-east-2.rds.amazonaws.com:5432/redditsaved'
# app.config['SQLALCHEMY_BINDS'] = {'other_schema': 'redditsaved'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# db.init_app(app) 
# migrate = Migrate(app ,db)

# migrate.init_app(app, db) 
# db.init_app(app)

from reddit_saved import routes
from reddit_saved.models import userinfo, savedposts