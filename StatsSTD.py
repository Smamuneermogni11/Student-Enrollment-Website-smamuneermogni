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

StatsSTD = Blueprint('StatsSTD', __name__)
app = Flask(__name__)

@StatsSTD.route('/StatsSTD', methods=['GET', 'POST']) 
def StatsSTDf():


               
              
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()
                user_id = current_user.id
                cur.execute("SELECT * FROM semester_view")
       
                current_Sem_Dec = cur.fetchall()
                
                con.commit()
                
                cur.execute("SELECT Count0 from std_comp0 where user_id = '%s'"% (user_id))
                std_comp0 = cur.fetchall()

                cur.execute("SELECT Count1 from std_comp1 where user_id = '%s'"% (user_id))
                std_comp1 = cur.fetchall()
               

                cur.execute("SELECT CountNull from std_compNull where user_id = '%s'"% (user_id))
                std_compNull = cur.fetchall()

                cur.execute("""select count(distinct course.course_id) as recourse from course
where course.dep_id in (select user.dep_id from user where user.id = ?) 
and course.course_id not in (select time_table.course_id from time_table where time_table.user_id = ? and time_table.complete = 1)
""",(user_id,user_id))
                recourse = cur.fetchall()
                
           

             
            


                con.commit()
                con.close()
                return render_template('StatsSTD.html',std_comp0=std_comp0,std_comp1=std_comp1,std_compNull=std_compNull,recourse=recourse, idd = current_user.id,name= current_user.name,current_Sem_Dec=current_Sem_Dec)

