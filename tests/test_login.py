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