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
import pandas as pd
import json
import plotly
import plotly.express as px

course_plan = Blueprint('course_plan', __name__)
app = Flask(__name__)

@course_plan.route('/course_plan', methods=['GET', 'POST']) 
def course_planf():


               
                user_id = request.form.get('iddc',type=int)
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()
                cur.execute("SELECT * FROM studen_course_info")
                Completed = cur.fetchall()

                cur.execute("""select course.course_id,course.course_code,course.course_name, 'Not Completed' as complete , course.level_id, semester.sem_dec from course

join semester on semester.sem_id = course.SEM
where course.dep_id in (select dep_id from user where id =?) and course.course_id not in (select course_id from time_table where complete = 1 and user_id = ?)""", (user_id,user_id))
       
                NotCompleted = cur.fetchall()
                
                con.commit()
                
        
                con.close()
                return render_template('course_plan.html',NotCompleted=NotCompleted,Completed=Completed, idd = current_user.id,name= current_user.name,current_Sem_Dec=current_Sem_Dec)

