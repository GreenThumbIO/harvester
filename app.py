import os
from dotenv import find_dotenv, load_dotenv
from flask import Flask
from models import db, connect_db
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)

    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or f'postgresql:///{DBNAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")

    connect_db(app)

    # test route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app

if __name__ == '__main__':
    app = create_app()

    app.run(debug=True, host='0.0.0.0', port=5000)
