import pytest
from main import create_app
from models import User
def test_home_page_post():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 405
        assert b"Home Page Test" not in response.data

def client(app):

    with app.test_client() as client:
        yield client

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

