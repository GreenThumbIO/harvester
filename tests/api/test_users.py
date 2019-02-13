"""
tests/test_api_users.py - Tests for the Users resource
"""
from werkzeug.exceptions import NotFound

from app.models import User
from app.exceptions import ValidationError

from ..base import BaseResourceTestCase
from ..factories import UserFactory


class UserResourceTest(BaseResourceTestCase):

    def get_user_url(self, id=1):
        return '/api/users/{}'.format(id)

    def test_get_nonexistent_user(self):
        url = self.get_user_url(id=1)

        with self.assertRaises(NotFound):
            response, response_json = self.client.get(url)
