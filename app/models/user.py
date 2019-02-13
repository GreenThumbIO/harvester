"""
app/models/user.py - The User model
"""
from passlib.apps import custom_app_context as pwd_context

from flask import url_for

from app import db
from app.exceptions import ValidationError

from .base import BaseModel

class User(BaseModel):
    """The User model"""

    __tablename__ = 'users'

    username = db.Column(db.String(100), nullable=False)
    crypted_password = db.Column(db.String(255), nullable=False)
    token = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<User id={}>'.format(self.id)
