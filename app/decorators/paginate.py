import functools
from flask import url_for, request
from flask_sqlalchemy import BaseQuery
from sqlalchemy import desc

from ..exceptions import ValidationError
from config import PER_PAGE


def paginate(collection, max_per_page=PER_PAGE):
    """Generate a paginated response for a resource collection.

    Routes that use this decorator must return a SQLAlchemy query as a
    response.

    The output of this decorator is a Python dictionary with the paginated
    results. The application must ensure that this result is converted to a
    response object, either by chaining another decorator or by using a
    custom response object that accepts dictionaries."""
    def decorator(f):

        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            # invoke the wrapped function
            query = f(*args, **kwargs)

            if not isinstance(query, BaseQuery):
                return query

            # entity (Cow, Pen, Farm, Barn)
            entity = query.column_descriptions[0].get('entity')

            # params
            data = request.args

            # which column to
            order_by = 'id'

            if 'order_by'in data:
                order_by_field = data.get('order_by')
                if order_by_field not in entity.order_by_fields:
                    raise ValidationError('Field `{}` is not available for '
                                          'ordering'.format(order_by_field))

                order_by = getattr(entity, order_by_field)

            # direction
            direction = str(data.get('direction')).lower() if 'direction' in data else None

            if direction == 'desc':
                query = query.order_by(desc(order_by))
            else:
                query = query.order_by(order_by)

            # LIMITING
            # obtain pagination arguments from the URL's query string
            page = request.args.get('page', 1, type=int)
            per_page = min(request.args.get('per_page', max_per_page,
                                            type=int), max_per_page)

            # run the query with Flask-SQLAlchemy's pagination
            p = query.paginate(page, per_page)

            # build the pagination metadata to include in the response
            pages = {'page': page, 'per_page': per_page,
                     'total': p.total, 'pages': p.pages}
            if p.has_prev:
                pages['prev_url'] = url_for(request.endpoint, page=p.prev_num,
                                            per_page=per_page,
                                            _external=True, **kwargs)
            else:
                pages['prev_url'] = None
            if p.has_next:
                pages['next_url'] = url_for(request.endpoint, page=p.next_num,
                                            per_page=per_page,
                                            _external=True, **kwargs)
            else:
                pages['next_url'] = None
            pages['first_url'] = url_for(request.endpoint, page=1,
                                         per_page=per_page, _external=True,
                                         **kwargs)
            pages['last_url'] = url_for(request.endpoint, page=p.pages,
                                        per_page=per_page, _external=True,
                                        **kwargs)

            # return a dictionary as a response
            return {collection: [item.to_dict() for item in p.items],
                    'pagination': pages}
        return wrapped
    return decorator
