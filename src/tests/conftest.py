""" Test Client Factory """
import pytest
from app import create_app


@pytest.fixture(scope='module')
def test_client():
    """ Test client is created to test against application """
    app = create_app(environment='testing')
    test_app = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield test_app

    ctx.pop()
