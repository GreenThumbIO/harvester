"""
app/api module defines API resources as HTTP endpoints
"""
from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
def index():
    return 'Harvester API'

from . import users # noqa
from . import error_handlers # noqa
