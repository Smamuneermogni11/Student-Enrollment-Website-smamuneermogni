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
                                data=dict(email='naif.alblawi@cgu.edu', password='123456'))
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
        
# cd C:\Users\MuneerMogni\Desktop\PythonByte edit\PythonByte
# venv\Scripts\activate.bat
# python -m main