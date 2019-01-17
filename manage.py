from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from models import Schedule

DBUSER="postgres"
DBPASS="greenthumb"
DBNAME="postgres"
DBPORT="5432"
DBHOST="db"
DBPORT="5432"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
    user=DBUSER,
    passwd=DBPASS,
    host=DBHOST,
    port=DBPORT,
    db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
