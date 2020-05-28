

from flask.ext.testing import TestCase

from app import create_app as sub_app_creation
from project.models import User, BlogPost


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        return sub_app_creation('testing', 'test_app')
