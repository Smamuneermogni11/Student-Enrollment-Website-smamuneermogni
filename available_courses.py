import sqlite3
from flask import Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_login import login_user, logout_user, login_required, current_user
from __init__ import db

available_courses = Blueprint('available_courses', __name__)
app = Flask(__name__)
with app.app_context():
    con = sqlite3.connect("instance/db.sqlite")

    cur = con.cursor()


    cur.execute("SELECT * FROM course")
    data = cur.fetchall()

    con.close()
@available_courses.route('/student_course_enrolment', methods=['GET', 'POST']) 
def student_course_enrolment():
    return render_template('student_course_enrolment.html', data=data)

  