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


semester = Blueprint('semester', __name__)
app = Flask(__name__)

@semester.route('/semester', methods=['GET', 'POST']) 
def semesterf():
    with app.app_context():
       
        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()
        cur.execute("SELECT * FROM semester")
        
        lec_dd = cur.fetchall()
        cur.execute("SELECT * FROM semester_view")
        current_Sem_Dec = cur.fetchall()[0][0]
        con.commit()
      
        if request.method=='POST':
            SEMp = request.form.get('lec_id')
            cur.execute("UPDATE  default_sem set default_sem = ? where default_id = ? " , (SEMp, 1))
            con.commit()
            cur.execute("SELECT * FROM semester_view")
            current_Sem_Dec = cur.fetchall()[0][0]

        
    




        con.close()
     
       

    return render_template('semester.html', lec_dd=lec_dd,current_Sem_Dec=current_Sem_Dec)