from app import create_app
import pytest
from app.drivers.db import factory as db_factory

@pytest.fixture
def db():
    db_instance = db_factory.create('memory', 100)
    return db_instance

@pytest.fixture
def client():
    app = create_app('testing','test_app')
    return app.test_client()