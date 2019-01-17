from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Schedule(db.Model):
    """Represents a feeding schedule"""

    __tablename__ = 'schedules'

    id = db.Column(
      db.Integer,
      primary_key=True
    )
    name = db.Column(
      db.String(80)
    )

    # @classmethod
    # def create(cls, name):
    #     """Creates a schedule."""


    #     schedule = Schedule(name=name)

    #     db.session.add(schedule)
    #     return schedule

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
