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
        





