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


@available_courses.route('/student_course_enrolment/', methods=['GET', 'POST']) 
def student_course_enrolment():
    with app.app_context():

        user_id =  request.args.get('iddt') 
        print('1')       
        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()      
        cur.execute("SELECT course_id, course_code, course_name, level_id, credit, Day_id , FromT, Tot FROM course p WHERE  NOT EXISTS (SELECT * FROM   Time_table od WHERE  p.course_id = od.course_id and od.user_id = '%s') AND dep_id = (select dep_id from user where id  = '%s' )" % (user_id,user_id))
        data = cur.fetchall()
        cur.execute("SELECT course.course_id, course.course_code, course.course_name, course.credit,course.day_id ,course.fromT, course.toT FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (user_id))
        data2 = cur.fetchall()
        cur.execute("SELECT sum(course.credit) FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (user_id))
        dataC = cur.fetchall()
        con.commit()
        con.close()
        print('2')   
    return render_template('student_course_enrolment.html', data=data,data2=data2, idd = current_user.id,name= current_user.name,dataC=dataC)

  