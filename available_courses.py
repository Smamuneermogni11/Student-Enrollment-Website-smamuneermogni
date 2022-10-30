import email
import sqlite3
from this import s
from types import NoneType
from flask import Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash,session
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from __init__ import db
from models import User
from flask_login import login_required, current_user,LoginManager
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db
import sqlite3
from flask import Flask

available_courses = Blueprint('available_courses', __name__)
app = Flask(__name__)

@available_courses.route('/student_course_enrolment', methods=['GET', 'POST']) 
def student_course_enrolment():
    with app.app_context():
        #if request.method == 'GET':
                #ee = request.form.get('course_id')
            #eee = request.form.get('idd')
        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()      
        #eee = request.form.get('idd').first()
        cur.execute("SELECT course_id,course_code,course_name,level_id,credit FROM course where dep_id = (select dep_id from user where id = '%s' ) " % 2)
        #cur.execute("SELECT course_id,course_code,course_name,level_id,credit FROM course where dep_id = (select dep_id from user where id = (?) ) " ,(1))
        data = cur.fetchall()
        
        con.commit()
        con.close()
    return render_template('student_course_enrolment.html', data=data, idd = current_user.id,name= current_user.name)

  