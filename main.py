
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db
from flask import Flask
import sqlite3


main = Blueprint('main', __name__)
app = Flask(__name__)
@main.route('/') 
def index():
   
    return render_template('index.html')

@main.route('/About') 
def About():
    
    return render_template('About.html')

@main.route('/new') 
def new():
    return render_template('new.html')

@main.route('/profile') 
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
    
@main.route('/base') 
@login_required
def base():
    return render_template('base.html', rol_id=current_user.rol_id)


    
app = create_app() 
if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
        app.run(debug=True)