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
#import plotly
#import plotly.express as px

Stats = Blueprint('Stats', __name__)
app = Flask(__name__)

@Stats.route('/Stats', methods=['GET', 'POST']) 
def Statsf():


               
              
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()
                cur.execute("SELECT default_sem FROM default_sem")
                SEM = cur.fetchone()[0]
                print(SEM)
                cur.execute("SELECT * FROM semester_view")
       
                current_Sem_Dec = cur.fetchall()
                
                con.commit()
                
                cur.execute("SELECT alls from count_of_all_students where sem = '%s'" % (SEM))
                dataAll = cur.fetchall()
                cur.execute("SELECT Nots from count_of_NOT_enrolled_student")
                dataNot = cur.fetchall()
                cur.execute("SELECT Enrolled from count_of_Enrolled_students where sem = '%s'" % (SEM))
                dataEnr = cur.fetchall()
                cur.execute("SELECT lecalls from count_of_all_lec where sem = '%s'" % (SEM))
                lecalls = cur.fetchall()
            


                con.commit()
                con.close()
                return render_template('Stats.html',dataAll=dataAll,dataNot=dataNot,dataEnr=dataEnr,lecalls=lecalls, idd = current_user.id,name= current_user.name,current_Sem_Dec=current_Sem_Dec)

