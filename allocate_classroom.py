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
allocate_classroom = Blueprint('allocate_classroom', __name__)
app = Flask(__name__)
@allocate_classroom.route('/allocate_classroomf', methods=['GET', 'POST']) 
def allocate_classroomf():
    with app.app_context():
       
        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()
        cur.execute("SELECT * FROM loc")
       
        classroom = cur.fetchall()
        con.commit()
        cur.execute("SELECT * FROM classroom_view")
        courses = cur.fetchall()
        course_id = request.form.get('course_id')
        con.commit()
        
        loc_id = request.form.get('classroom')
        print("loc_idss")
        print(loc_id)






        cur.execute("UPDATE  course set loc_id = ? where course_id = ? " , (loc_id, course_id))
        con.commit()
        cur.execute("SELECT * FROM classroom_view")
        courses = cur.fetchall()
        con.commit()
        con.close()
     
       

    return render_template('allocate_classroom.html', classroom=classroom,courses=courses)


    

