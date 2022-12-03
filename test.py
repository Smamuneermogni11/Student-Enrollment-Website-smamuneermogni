from pip import main
import pytest

from main import create_app
from models import User


def test_home_page_post():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 405
        assert b"Home Page Test" not in response.data

def test_home_page_get():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/')

        assert response.status_code == 200
        assert b"Home Page Test" not in response.data



def test_valid_login_logout():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
        response = test_client.get('/profile')
        assert response.status_code == 200
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
 

def test_invalid_login():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/login',
                                    data=dict(email='naif.alblawi@cgu.edu', password='1111'))
        response = test_client.get('/login')
        assert response.status_code == 200


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()  
        
# cd C:\Users\MuneerMogni\Desktop\PythonByte edit\PythonByte
# venv\Scripts\activate.bat
# python -m main