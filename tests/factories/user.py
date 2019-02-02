"""
tests/factories/user.py - This is a User Factory
"""
import factory

from app import db
from app.models import User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    username = factory.Faker('user_name')
    crypted_password = factory.Faker('password')
    token = factory.Faker('password')
