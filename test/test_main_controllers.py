
import pytest
from flask import Response

def test_get_all(client):
    response = client.get("/endpoint/")
    assert response.status_code == 200

def test_get_by_resource(client):
    response = client.get("/endpoint/resource")
    assert response.status_code == 200

def test_post(client):
    response = client.post("/endpoint/resource")
    assert response.status_code == 201


def test_delete(client):
    response = client.delete("/endpoint/resource")
    assert response.status_code == 202


