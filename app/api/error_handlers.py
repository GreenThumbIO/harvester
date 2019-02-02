"""
app/api/errorhandlers.py - All app error handlers are defined here.
"""
from flask import jsonify
from app.exceptions import ValidationError

from . import api


BAD_REQUEST = 400
FORBIDDEN = 403
NOT_FOUND = 404
INTERNAL_SERVER_ERROR = 500


@api.app_errorhandler(ValidationError)
def validation_error(e):
    message = e.args[0] if e.args else ''
    response = jsonify({'status': BAD_REQUEST, 'error': 'Bad request',
                        'message': message})
    response.status_code = BAD_REQUEST
    return response


@api.app_errorhandler(NOT_FOUND)
def not_found(e):
    response = jsonify({'status': NOT_FOUND, 'error': 'Not found',
                        'message': 'Resource not found'})
    response.status_code = NOT_FOUND
    return response


@api.app_errorhandler(FORBIDDEN)
def forbidden(e):
    response = jsonify({'status': FORBIDDEN, 'error': 'Forbidden',
                        'message': 'Not authorized'})
    response.status_code = FORBIDDEN
    return response


@api.app_errorhandler(INTERNAL_SERVER_ERROR)
def internal_server_error(e):
    message = e.args[0] if e.args else ''
    response = jsonify({'status': INTERNAL_SERVER_ERROR,
                        'error': 'Internal server error',
                        'message': message})
    response.status_code = INTERNAL_SERVER_ERROR
    return response
