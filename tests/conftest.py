import pytest
from application.main import app

@pytest.fixture
def client():
    return app.test_client()
