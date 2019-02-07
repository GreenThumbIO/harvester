from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Schedule(db.Model):
    """Represents a feeding schedule"""

    __tablename__ = 'schedules'

    id = db.Column( db.Integer, primary_key=True)
    name = db.Column( db.String(80), nullable=False)
    frequency = db.Column( db.String(30), nullable=False)
    manufacturer_id = db.Column( db.Integer, db.ForeignKey('manufacturers.id', 
        ondelete='CASCADE'), nullable=False)

    # add backref='schedule' and lazy='dynamic'?
    feedings = db.relationship('Feeding', backref='schedule', lazy='dynamic')
