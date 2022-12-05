from pip import main
import pytest
import json
import os
from main import create_app
from models import User
import tempfile
from __init__ import db
from flask import Flask, session,template_rendered
from flask_login import login_required, current_user

from contextlib import contextmanager
with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')





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

def test_access_current_user_id():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
        assert current_user.id == 1


def test_logout_redirect():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get("/logout", follow_redirects=True)
        assert response.request.path == "/login"

def test_invalid_login():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/login',
                                    data=dict(email='naif.alblawi@admin.edu', password='1111'))
        response = test_client.get('/login')
        assert response.status_code == 200



def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here



def client(app):
    return app.test_client()



def runner(app):
    return app.test_cli_runner()  
        





