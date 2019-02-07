from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dosage(db.Model):
    """Represents one dosage of a product with amount, product id, and feeding
    id that controls the dosage amount"""

    __tablename__ = 'dosages'

    id = db.Column( db.Integer, primary_key=True)
    feeding_id = db.Column( db.Integer, db.ForeignKey('feedings.id', 
        ondelete='CASCADE'), nullable=False)
    product_id = db.Column( db.Integer, db.ForeignKey('products.id',
        ondelete='CASCADE'), nullable=False)
