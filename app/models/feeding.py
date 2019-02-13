from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Feeding(db.Model):
    """Represents one feeding event on a schedule"""

    __tablename__ = 'feedings'

    id = db.Column( db.Integer, primary_key=True)
    schedule_id = db.Column( db.Integer, db.ForeignKey('schedules.id', 
        ondelete='CASCADE'), nullable=False)
    order = db.Column( db.Integer, nullable=False)
