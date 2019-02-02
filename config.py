"""
config.py - This is where all configs for each environment will be defined.
"""
import os

from dotenv import find_dotenv, load_dotenv
from app.constants import TEST, STAGING, PRODUCTION, ENVIRONMENTS, DEVELOPMENT

try:
    load_dotenv(find_dotenv(raise_error_if_not_found=True))
except IOError:
    pass

try:
    RUNTIME = os.environ['RUNTIME'].lower()
except KeyError:
    raise RuntimeError('RUNTIME environment variable is not defined.')

# if is an invalid RUNTIME name, let's raise an error right way
if RUNTIME not in ENVIRONMENTS:
    raise RuntimeError('Invalid RUNTIME environment variable value: {}'.format(RUNTIME))

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = int(os.environ.get('SQLALCHEMY_ECHO', 0))
PER_PAGE = os.environ.get('PER_PAGE', 50)
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

if RUNTIME in (TEST, DEVELOPMENT):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

elif RUNTIME in (STAGING, PRODUCTION):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s: %(message)s',
        },
        'simple': {
            'format': '%(levelname)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'harvester.worker': {
            'level': 'ERROR',
            'handlers': ['console']
        }
    }
}
