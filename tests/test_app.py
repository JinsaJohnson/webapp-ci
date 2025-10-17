import pytest
from src.app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello, CI Pipeline with Python!" in response.data
