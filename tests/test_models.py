"""Model unit tests."""

# run these in docker with the command
#
#    docker-compose run web python -m unittest ./tests/test_schedule_model.py

import os
from unittest import TestCase

from models import db, Schedule, Feeding

# os.environ['DATABASE_URL'] = 'postgresql:///harvester-test'

from app import create_app

class ScheduleModelTestCase(TestCase):
    """Test schedule model."""

    def setUp(self):
        """Create test client, add sample data."""
        
        app = create_app()

        db.drop_all()
        db.create_all()

        Schedule.query.delete()

        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        """Drops database tables"""

        db.session.commit()
        db.drop_all()
    
    def test_schedule_model(self):
        """Does basic model work?"""
        s = Schedule(id=0, name='secnd', frequency='weekly')
        
        db.session.add(s)
        db.session.commit()

        self.assertEqual(s.name, "secnd")

        
class FeedingModelTestCase(TestCase):
    """Test feeding model."""

    def setUp(self):
        """Create test client, add sample data."""
        
        app = create_app()

        db.drop_all()
        db.create_all()

        Feeding.query.delete()
        Schedule.query.delete()

        schedule = Schedule(name='secnd', frequency='weekly')

        db.session.add(schedule)        
        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        """Drops database tables"""        

        db.session.commit()
        db.drop_all()
    
    def test_feeding_model(self):
        """Does basic model work?"""

        schedule = Schedule.query.all()[0]

        feedings = [Feeding(schedule_id=schedule.id, order=n) for n in range(1,13)]
        schedule.feedings = feedings
        
        db.session.add(schedule)
        db.session.commit()

        feedings = [Feeding.query.get_or_404(f.id) for f in feedings]

        for i, feeding in enumerate(feedings):
            self.assertEqual(feeding.order, i+1)
            self.assertEqual(feeding.schedule.id, schedule.id)


