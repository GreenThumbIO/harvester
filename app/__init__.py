"""
app/__init__.py - Main application module
"""
import os
from logging.config import dictConfig

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# import models so they are registered for SQLAlchemy
from . import models  # noqa

# encoders
from .encoders.json import AppJSONEncoder  # noqa

# template dir
template_dir = os.path.join(os.path.abspath('.'), 'app/templates')


def create_app():

    app = Flask(__name__, template_folder=template_dir)

    # overriding settings
    app.config.from_pyfile('../config.py')
    config = app.config

    # logging
    dictConfig(config['LOGGING'])

    # our custom json encoder
    app.json_encoder = AppJSONEncoder

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # initialize blueprints
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
