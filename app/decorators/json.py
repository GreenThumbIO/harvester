import functools
from flask import jsonify


def json(f):
    """Generate a JSON response from a database model or a Python
    dictionary."""
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        # invoke the wrapped function
        rv = f(*args, **kwargs)

        # the wrapped function can return the dictionary alone,
        # or can also include a status code and/or headers.
        # here we separate all these items
        status = None
        headers = None
        if isinstance(rv, tuple):
            rv, status, headers = rv + (None,) * (3 - len(rv))
        if isinstance(status, (dict, list)):
            headers, status = status, None

        # if the response was a database model, then convert it to a
        # dictionary
        if not isinstance(rv, dict):
            if hasattr(rv, 'to_dict'):
                rv = rv.to_dict()
            else:
                return rv

        # generate the JSON response
        # this's a hack to rename table name to 'objects' in json resp
        # for key, value in rv.items():
        #    if key is not 'pagination':
        #        rv['objects'] = rv[key]
        #        rv.pop(key, None)
        #        break
        rv = jsonify(rv)
        if status is not None:
            rv.status_code = status
        if headers is not None:
            rv.headers.extend(headers)
        return rv
    return wrapped
