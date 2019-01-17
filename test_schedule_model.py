"""Schedule model tests."""

# run these tests like:
#
#    python3 -m unittest test_schedule_model.py

import os
from unittest import TestCase

from models import db, Schedule

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

# os.environ['DATABASE_URL'] = 'postgresql:///harvester-test'


# Now we can import app

from app import create_app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data



class ScheduleModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""
        app = create_app()
        db.create_all()

        Schedule.query.delete()

        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        """Removes all data from database tables"""

        Schedule.query.delete()

        db.session.commit()
    
    def test_schedule_model(self):
        """Does basic model work?"""
        s = Schedule(id=0, name='secnd')
        
        db.session.add(s)
        db.session.commit()

        self.assertEqual(s.name, "secnd")

