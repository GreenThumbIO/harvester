"""
app/api/users.py - User API Resource HTTP Endpoints
"""
from flask import request

from app import db
from app.models import User
from app.decorators import json

from . import api

@api.route('/users/<int:id>', methods=['GET'])
@json
def get_user(id):
    """
    Returns the user with the specified id.
    """
    user = User.query.get_or_404(id)
    return user.to_dict()
