"""
tests/test_client.py - This module has helper class client
in making requests for testing.
"""
import gzip
import json
from io import BytesIO

from datetime import datetime

from urllib.parse import urlsplit, urlunsplit, urlencode


class TestClient:
    def __init__(self, app, token_type='Bearer', token=None):
        self.app = app
        self.auth = '{} {}'.format(token_type, token) if token else None

    def send(self, url, method='GET', data=None, headers={}, gzipped=False):
        # for testing, URLs just need to have the path and query string
        url_parsed = urlsplit(url)
        url = urlunsplit(('', '', url_parsed.path, url_parsed.query,
                          url_parsed.fragment))

        # append the authentication headers to all requests
        headers = headers.copy()
        if self.auth:
            headers['Authorization'] = self.auth
        headers['Content-Type'] = 'application/json'
        headers['Accept'] = 'application/json'

        # convert JSON data to a string
        if data:
            for k, v in data.items():
                if isinstance(v, datetime):
                    data[k] = v.strftime('%Y-m-%dT%H:%M:%SZ')
            data = json.dumps(data)

        if gzipped:
            data = data + "\n"
            data = self._gzip_compress(data)
            headers['Content-Encoding'] = 'gzip'
            headers['Content-Length'] = len(data)

        # send request to the test client and return the response
        with self.app.test_request_context(url, method=method, data=data,
                                           headers=headers):
            rv = self.app.preprocess_request()
            if rv is None:
                rv = self.app.dispatch_request()
            rv = self.app.make_response(rv)
            rv = self.app.process_response(rv)
            return rv, json.loads(rv.data.decode('utf-8'))

    def get(self, url, params=None, headers={}):
        parameters = urlencode(params) if params else None
        if parameters:
            url = '{}?{}'.format(url, parameters)
        return self.send(url, 'GET', headers=headers)

    def post(self, url, data, headers={}, gzipped=False):
        return self.send(url, 'POST', data, headers=headers, gzipped=gzipped)

    def put(self, url, data, headers={}, gzipped=False):
        return self.send(url, 'PUT', data, headers=headers, gzipped=gzipped)

    def patch(self, url, data, headers={}):
        return self.send(url, 'PATCH', data, headers=headers)

    def delete(self, url, headers={}):
        return self.send(url, 'DELETE', headers=headers)

    def _gzip_compress(self, data):
        gzip_buffer = BytesIO()
        with gzip.GzipFile(mode='wb',
                           compresslevel=self.app.config['COMPRESS_LEVEL'],
                           fileobj=gzip_buffer) as gzip_file:
            data_bytes = data.encode('utf-8')
            gzip_file.write(data_bytes)
        return gzip_buffer.getvalue()
