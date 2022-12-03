from pip import main
import pytest

from main import create_app

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
