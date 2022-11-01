import email
import sqlite3
from this import s
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

insert_course = Blueprint('student_course_enrolment', __name__)
app = Flask(__name__)

@insert_course.route('/incourse', methods=['GET', 'POST']) 
def incourse():
        #with app.app_context():
            
            #if request.method == 'POST':
                ee = request.form.get('course_id')
                #eee = request.form.get('idd')
                eee = 1
                #request.form['submit_button'] == 'Do Something':
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()

                cur.execute("insert into Time_table (user_id,course_id) values (?,?)", (eee, ee) )
                con.commit()
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()      
  
                cur.execute("SELECT course_id,course_code,course_name,level_id,credit FROM course where dep_id = (select dep_id from user where id  = '%s' ) " % (eee))
                data = cur.fetchall()
                
                cur.execute("SELECT course.course_code, course.course_name FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (eee))
                data2 = cur.fetchall()
                con.commit()
                con.close()
                return render_template('student_course_enrolment.html',data=data,data2=data2, idd = current_user.id,name= current_user.name)

