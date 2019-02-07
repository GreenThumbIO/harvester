from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Device(db.Model):
    """Represents a single device, which contains information about who and
    where a device is registered to, as well as its core identification"""

    __tablename__ = 'devices'

    id = db.Column( db.Integer, primary_key=True)
    name = db.Column( db.String(80), nullable=False)
    address = db.Column( db.String(80), nullable=False)
    registered_at = db.Column( db.DateTime, nullable=False, 
            default=datetime.utcnow(),)
    registered_by = db.Column( db.Integer, nullable=True)
    projects = db.relationship("Project",
            secondary=association_table,
            backref="devices")
