from datetime import datetime
import email
import sqlite3
from this import s
from flask import Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash,session, Response
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
from fpdf import FPDF

complete = Blueprint('complete', __name__)
app = Flask(__name__)

@complete.route('/complete', methods=['GET', 'POST']) 
def completef():
         
            user_id = current_user.id
               
            con = sqlite3.connect("instance/db.sqlite")
            cur = con.cursor()
            cur.execute("SELECT default_sem FROM default_sem")
            SEM = cur.fetchone()[0]
            con.commit()
            cur.execute("SELECT * from student_list where lec_id = '%s'" % (user_id))
            data2 = cur.fetchall()

            course_idP = request.form.get('Pass')
            course_idF = request.form.get('Fail')
            course_idN = request.form.get('nograde')

            #if request.method == 'POST':
            Pass = request.form.get('Pass', None)
            Fail = request.form.get('Fail', None)
            nograde = request.form.get('nograde', None)
            #Nullvalue = None

            if Pass:
                cur.execute("UPDATE  Time_table set complete = ? where course_id = ? " , (True, course_idP))
                con.commit()
            elif Fail:
                cur.execute("UPDATE  Time_table set complete = ? where course_id = ?" , (False, course_idF))
                con.commit()
            elif nograde:
                cur.execute("UPDATE  Time_table set complete = ? where course_id = ?" , (None, course_idN))
                con.commit()


            cur.execute("SELECT * from student_list where lec_id = '%s'" % (user_id))
            data2 = cur.fetchall()    
                


            con.commit()

            con.close()

            return render_template('complete.html',data2=data2, idd = current_user.id,name= current_user.name)
                


              