from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

db = SQLAlchemy()

class Project(db.Model):
    """Represents a single project, which contains a name start timestamp,
    ending timestamp and feeding schedule assigned to the project"""

    __tablename__ = 'projects'

    id = db.Column( db.Integer, primary_key=True)
    schedule_id = db.Column( db.Integer, db.ForeignKey('schedules.id',
        ondelete='CASCADE'), nullable=False)
    name = db.Column( db.String(80), nullable=False)
    started_at = db.Column( db.DateTime, nullable=False, 
            default=datetime.utcnow())
    ended_at = db.Column( db.DateTime, nullable=True)

association_table = db.Table('projectdevices', Base.metadata,
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id')),
    db.Column('device_id', db.Integer, db.ForeignKey('devices.id'))
)