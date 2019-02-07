from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Manufacturer(db.Model):
    """Represents a single manufacturer of a product with name and id"""

    __tablename__ = 'manufacturers'

    id = db.Column( db.Integer, primary_key=True)
    name = db.Column( db.String(80), nullable=False)
