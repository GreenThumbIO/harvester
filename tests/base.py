"""
tests/base.py - This is the base test module for the tests.
"""
import unittest

from app import create_app, db as app_db
from app.models import User

from . import TestClient

class BaseResourceTestCase(unittest.TestCase):
    app = create_app()
    db = app_db

    def setUp(self):
        # initialize the testing application
        self.app = create_app()
        self.ctx = self.app.app_context()
        self.ctx.push()

        self.user = User.query.get(1)
        self.client = TestClient(self.app)

    def tearDown(self):
        self.ctx.pop()


class BaseModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.ctx = self.app.app_context()
        self.ctx.push()

        self.app.config['RUNTIME'] = 'test'
        self.app.config['SERVER_NAME'] = 'testing'

        app_db.drop_all()
        app_db.create_all()

    def tearDown(self):
        app_db.session.remove()
        app_db.drop_all()
        app_db.get_engine(self.app).dispose()
        self.ctx.pop()

    def create_relationship(self, parent, child):
        relationship = parent.relate(child)
        app_db.session.add(relationship)
        app_db.session.commit()

    def delete_relationship(self, parent, child):
        unrelate = parent.unrelate(child)
        app_db.session.add(unrelate)
        app_db.session.commit()
