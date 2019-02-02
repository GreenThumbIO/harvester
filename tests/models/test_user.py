"""
harvester/tests/models/test_user.py - This module contains all the tests for the User model
"""
from app import db
from app.models import User
from app.exceptions import ValidationError

from ..base import BaseModelTestCase
from ..factories import UserFactory

class UserTest(BaseModelTestCase):
    def setUp(self):
        super(UserTest, self).setUp()

        UserFactory(username='tester')
        db.session.commit()


    def test_truth(self):
        self.assertEqual(User.query.get(1).id, 1)
