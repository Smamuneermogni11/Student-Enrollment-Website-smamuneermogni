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