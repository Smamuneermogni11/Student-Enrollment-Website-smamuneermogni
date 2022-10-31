import pytest

from main import create_app
from models import User


def test_home_page_post():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 405
        assert b"Home Page Test" not in response.data

@pytest.fixture(scope="session")
def app(request, monkeypatch_session):
    monkeypatch_session.setenv("FLASK_ENV", "testing")
    app = create_app()
    return app

def client(app):

    with app.test_client() as client:
        yield client

@pytest.fixture(scope="session")
def monkeypatch_session(request):

    from _pytest.monkeypatch import MonkeyPatch

    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()

# def test_new_user():
#     """
#     GIVEN a User model
#     WHEN a new User is created
#     THEN check the email, hashed_password, and role fields are defined correctly
#     """
#     user = User('1')
#     assert user.email == 'naif@gmail.com'
#     assert user.hashed_password != 'Password!!'
#     assert user.rol_id == '1'

