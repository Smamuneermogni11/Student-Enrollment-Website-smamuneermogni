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




allocate_classroom = Blueprint('allocate_classroom', __name__)
app = Flask(__name__)
@allocate_classroom.route('/allocate_classroomf', methods=['GET', 'POST']) 
def allocate_classroomf():
    with app.app_context():
        
        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()
        cur.execute("SELECT default_sem FROM default_sem")
        SEM = cur.fetchone()[0]
        con.commit()
        cur.execute("SELECT * FROM loc")
       
        classroom = cur.fetchall()
        con.commit()
        cur.execute("SELECT * FROM classroom_view")
        courses = cur.fetchall()
        course_id = request.form.get('course_id')
        con.commit()
        nolec = request.form.get('nolec', None)
        loc_id = request.form.get('classroom')
        print("loc_idss")
        print(loc_id)
        cur.execute(""" SELECT distinct

    cp1.Day_id AS CP1_Day_id,
    cp1.loc_id AS CP1_loc_id,
    cp1.fromT AS CP1_fromT,
    cp1.toT AS CP1_toT,
    cp1.SEM AS CP1_SEm,
    cp2.Day_id AS CP2_Day_id,
    cp2.loc_id AS CP2_loc_id,
    cp2.fromT AS CP2_fromT,
    cp2.toT AS CP2_toT,
    cp2.SEM AS CP2_SEm
FROM 
    course AS cp1
JOIN
    course AS cp2 
    ON cp2.course_id = cp1.course_id AND cp2.SEM = cp1.SEM
    
      And (cp2.fromT >= cp1.fromT and cp2.fromT < cp1.toT AND  cp1.fromT <= cp2.fromT and cp2.day_id = cp1.day_id)
      OR (cp2.toT > cp1.fromT and cp2.toT <= cp1.toT AND cp1.fromT <= cp2.fromT and cp2.day_id = cp1.day_id )
      OR (cp2.fromT <= cp1.fromT and cp2.toT >= cp1.toT AND cp1.fromT <= cp2.fromT and cp2.day_id = cp1.day_id)
      OR (cp2.fromT <= cp1.toT    and cp2.toT >= cp1.fromT  and cp2.day_id = cp1.day_id)
     
      where cp2.loc_id = ? AND cp1.SEM = ? and  cp1.course_id = ?  """, (loc_id,SEM,course_id))
        entry = cur.fetchone()
        error=''
        if request.method == 'POST':
            if entry is None:
                if course_id:
                    cur.execute("UPDATE  course set loc_id = ? where course_id = ? " , (loc_id, course_id))
                    con.commit()
                    error = "The Classroom has been added successfully. "
                if nolec:
                    course_idF = request.form.get('nolec')
                    cur.execute("UPDATE  course set loc_id = ? where course_id = ? " , (None, course_idF))
                    con.commit()
                    error = "The Classroom has been deleted successfully. "
                     
            else:
                error = "There is a time conflict. Choose another Classroom."



        #cur.execute("UPDATE  course set loc_id = ? where course_id = ? " , (loc_id, course_id))
        #con.commit()
        cur.execute("SELECT * FROM classroom_view")
        courses = cur.fetchall()
        con.commit()
        con.close()
     
       

    return render_template('allocate_classroom.html', classroom=classroom,courses=courses,error=error)


    

