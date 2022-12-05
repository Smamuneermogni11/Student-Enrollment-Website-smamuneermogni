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
                                    data=dict(name_loc='naif.alblawi@admin.edu', cap='1111'))
        response = test_client.get('/login')
        assert response.status_code == 200

def test_saverloc():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/saverloc',
                                    data=dict(name_loc='Test H 700', cap='60'))
        response = test_client.get('/saverloc')
        assert response.status_code == 200

def test_del_loc():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/del_loc',
                                    data=dict(locid='10'))
        response = test_client.get('/del_loc')
        assert response.status_code == 200

def test_add_course():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        
        response = test_client.post('/add_coursef',
                                    data=dict(CourseCode='CSC 250', CourseName='Information Technology',CourseDescription='Information Technology',Department='3',Plan='1',Level='1',Credit='4',Day='1',From='8:00',To='12:00',Semester='222'))
        response = test_client.get('/add_coursef')
        assert response.status_code == 200

def test_profile():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
        response = test_client.post('/profile',
                                    data=dict(name= current_user.name))
        response = test_client.get('/profile')
        assert response.status_code == 200
        assert current_user.name == 'Naif'


def test_del_course():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/del_course',
                                    data=dict(CourseID='200'))
        response = test_client.get('/del_course')
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
        





