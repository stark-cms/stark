import pytest

from api.app import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config['SERVER_NAME'] = 'localhost.localdomain'
    app_context = app.app_context()
    app_context.push()
    return app


@pytest.fixture
def client(app):
    with app.test_client() as c:
        yield c
