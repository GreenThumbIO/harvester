from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Schedule(db.Model):
    """Represents a feeding schedule"""

    __tablename__ = 'schedules'

    id = db.Column(
      db.Integer,
      primary_key=True
    )
    name = db.Column(
      db.String(80),
      nullable=False
    )
    frequency = db.Column(
      db.String(30),
      nullable=False
    )
    manufacturer_id = db.Column(
      db.Integer,
      db.ForeignKey('manufacturers.id', ondelete='CASCADE'),
      nullable=False
    )

    # add backref='schedule' and lazy='dynamic'?
    feedings = db.relationship('Feeding', backref='schedule', lazy='dynamic')

class Feeding(db.Model):
    """Represents one feeding event on a schedule"""

    __tablename__ = 'feedings'

    id = db.Column(
      db.Integer,
      primary_key=True
    )
    schedule_id = db.Column(
      db.Integer,
      db.ForeignKey('schedules.id', ondelete='CASCADE'),
      nullable=False
    )
    order = db.Column(
      db.Integer,
      nullable=False
    )

class Dosage(db.Model):
    """Represents one dosage of a product with amount, product id, and feeding
    id that controls the dosage amount"""

    __tablename__ = 'dosages'

    id = db.Column(
      db.Integer,
      primary_key=True
    )
    feeding_id = db.Column(
      db.Integer,
      db.ForeignKey('feedings.id', ondelete='CASCADE'),
      nullable=False
    )
    product_id = db.Column(
      db.Integer,
      db.ForeignKey('products.id', ondelete='CASCADE'),
      nullable=False
    )

class Product(db.Model):
    """Represents a single product with name, macro_nutrients and fk to
    manufacturer"""

    __tablename__ = 'products'

    id = db.Column(
      db.Integer,
      primary_key=True
    )
    name = db.Column(
      db.String(80),
      nullable=False
    )
    macro_nutrients = db.Column(
      db.String(80),
      nullable=True
    )
    manufacturer_id = db.Column(
      db.Integer,
      db.ForeignKey('manufacturers.id', ondelete='CASCADE'),
      nullable=False
    )

class Manufacturer(db.Model):
    """Represents a single manufacturer of a product with name and id"""

    __tablename__ = 'manufacturers'

    id = db.Column(
      db.Integer,
      primary_key=True
    )
    name = db.Column(
      db.String(80),
      nullable=False
    )

class Project(db.Model):
    """Represents a single project, which contains a name start timestamp,
    ending timestamp and feeding schedule assigned to the project"""

    __tablename__ = 'projects'

    id = db.Column(
      db.Integer,
      primary_key=True
    )
    schedule_id = db.Column(
      db.Integer,
      db.ForeignKey('schedules.id', ondelete='CASCADE'),
      nullable=False
    )
    name = db.Column(
      db.String(80),
      nullable=False
    )
    started_at = db.Column(
      db.DateTime,
      nullable=False,
      default=datetime.utcnow(),
    )
    ended_at = db.Column(
      db.DateTime,
      nullable=True
    )

class Device(db.Model):
    """Represents a single device, which contains information about who and
    where a device is registered to, as well as its core identification"""

    __tablename__ = 'devices'

    id = db.Column(
      db.Integer,
      primary_key=True
    )
    name = db.Column(
      db.String(80),
      nullable=False
    )
    address = db.Column(
      db.String(80),
      nullable=False
    )
    registered_at = db.Column(
      db.DateTime,
      nullable=False,
      default=datetime.utcnow(),
    )
    registered_by = db.Column(
      db.Integer,
      nullable=True
    )

    # What projects is a device associated with
    projects = db.relationship(
      "Device",
      secondary="projectdevices",
      primaryjoin=(ProjectDevice.device_id == id),
      secondaryjoin=(ProjectDevice.project_id == "projects.id"),
      backref=db.backref('projects', lazy='dynamic'),
      lazy='dynamic')

class ProjectDevice(db.Model):
    """Connection of a device <-> project """

    __tablename__ = 'projectdevices'

    project_id = db.Column(
      db.Integer,
      db.ForeignKey('projects.id', ondelete='CASCADE'),
      primary_key=True,
    )
    device_id = db.Column(
      db.Integer,
      db.ForeignKey('devices.id', ondelete='CASCADE'),
      primary_key=True,
    )

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
