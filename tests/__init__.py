"""
The tests module
"""
import sys
import pytest

from .client import TestClient  # noqa
from .base import BaseResourceTestCase  # noqa


def run():
    result = pytest.main(['-x', '-vvv', 'tests'])
    sys.exit(result)
