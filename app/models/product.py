from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    """Represents a single product with name, macro_nutrients and fk to
    manufacturer"""

    __tablename__ = 'products'

    id = db.Column( db.Integer, primary_key=True)
    name = db.Column( db.String(80), nullable=False)
    macro_nutrients = db.Column( db.String(80), nullable=True)
    manufacturer_id = db.Column( db.Integer, db.ForeignKey('manufacturers.id', 
        ondelete='CASCADE'), nullable=False)
