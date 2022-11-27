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
allocate_lecturer = Blueprint('allocate_lecturer', __name__)
app = Flask(__name__)
@allocate_lecturer.route('/allocate_lecturerf', methods=['GET', 'POST']) 
def allocate_lecturerf():
    with app.app_context():
        SEM = 223
        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()
        cur.execute("SELECT * FROM user where rol_id = 2")
       
        lec_dd = cur.fetchall()
        con.commit()
        cur.execute("SELECT * FROM lecturer_view")
        lecturer = cur.fetchall()
        course_id = request.form.get('course_id')
        con.commit()
        
        lec_id = request.form.get('lec_id')
        print("lec_idss")
        print(lec_id)
        cur.execute(""" SELECT distinct

    cp1.Day_id AS CP1_Day_id,
    cp1.lec_id AS CP1_lec_id,
    cp1.fromT AS CP1_fromT,
    cp1.toT AS CP1_toT,
    cp1.SEM AS CP1_SEm,
    cp2.Day_id AS CP2_Day_id,
    cp2.lec_id AS CP2_lec_id,
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
     
      where cp2.lec_id = ? AND cp1.SEM = ? and  cp1.course_id = ?  """, (lec_id,SEM,course_id))
        entry = cur.fetchone()

        if entry is None:
            cur.execute("UPDATE  course set lec_id = ? where course_id = ? " , (lec_id, course_id))
            con.commit()
            error = "The lecturer has been added successfully. "
                     
        else:
            error = "There is a time conflict. Choose another lecturer."



        #cur.execute("UPDATE  course set loc_id = ? where course_id = ? " , (loc_id, course_id))
        #con.commit()
        cur.execute("SELECT * FROM lecturer_view")
        lecturer = cur.fetchall()
        con.commit()
        con.close()
     
       

    return render_template('allocate_lecturer.html', lec_dd=lec_dd,lecturer=lecturer,error=error)


    

