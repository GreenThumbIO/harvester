"""
app/models/base.py - This module holds the BaseModel used by every model.
"""
from datetime import datetime

from sqlalchemy import inspect

from app import db


class BaseModel(db.Model):
    """
    BaseModel with the basic fields for the models.
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow,
                           onupdate=datetime.utcnow)

    # assist jsonify to convert timestamps, otherwise tests fail
    def to_dict(self):
        inspection = inspect(self)
        columns = inspection.mapper.column_attrs
        fields = {}
        for column in columns:
            fields[column.key] = getattr(self, column.key)
        if hasattr(self, 'get_url'):
            fields['self_url'] = self.get_url()
        return fields

    def delete(self):
        db.session.delete(self)
        db.session.commit()
