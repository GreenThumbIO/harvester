"""
app/encoders/json.py JSON Encoder for consistent response handling
"""
from flask import current_app as app
from datetime import datetime, date
from flask.json import JSONEncoder


class AppJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                value = obj.strftime(app.config['DATETIME_FORMAT'])
                return value
            elif isinstance(obj, date):
                value = obj.strftime('%Y-%m-%d')
                return value
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
