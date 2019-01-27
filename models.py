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
      db.String(80),
      nullable=False
    )
    frequency = db.Column(
      db.String(30),
      nullable=False
    )

    # manufacturer_id

    # add backref='schedule' and lazy='dynamic'?
    feedings = db.relationship('Feeding', backref='schedule')

class Feeding(db.Model):
    """Represents one feeding event on a schedule"""

    __tablename__ = 'feedings'

    id = db.Column(
      db.Integer,
      primary_key=True
    )
    schedule_id = db.Column(
      db.Integer,
      nullable=False
      db.ForeignKey('schedules.id', ondelete='CASCADE')
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
      nullable=False
      db.ForeignKey('feedings.id', ondelete='CASCADE')
    )
    product_id = db.Column(
      db.Integer,
      nullable=False
      db.ForeignKey('products.id', ondelete='CASCADE')
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
      nullable=False
      db.ForeignKey('manufacturers.id', ondelete='CASCADE')
    )

class Manufacturer(db.Model):
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

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
