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
Timetable_lecturer = Blueprint('Timetable_lecturer', __name__)
app = Flask(__name__)

@Timetable_lecturer.route('/Timetable_lecturerf', methods=['GET', 'POST']) 
def Timetable_lecturerf():
                SEM = 223
                user_id = request.form.get('iddc',type=int)
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()
     
                cur.execute("SELECT course_id, course_code, course_name, level_id, credit , Day_id , FromT, Tot FROM course p WHERE  NOT EXISTS (SELECT * FROM   Time_table od WHERE  p.course_id = od.course_id and od.user_id = '%s' and od.sem = '%s') AND dep_id = (select dep_id from user where id  = '%s' ) " % (user_id,SEM,user_id))
                #cur.execute("SELECT course_id,course_code,course_name,level_id,credit FROM course where dep_id = (select dep_id from user where id  = '%s' ) " % (user_id))
                data = cur.fetchall()
                
                cur.execute("SELECT course.course_id, course.course_code, course.course_name, course.credit, course.day_id ,course.fromT, course.toT FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s' and Time_table.SEM = '%s'" % (user_id,SEM))
                data2 = cur.fetchall()
                cur.execute("SELECT sum(course.credit) FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s' and Time_table.SEM = '%s'" % (user_id, SEM))
                dataC = cur.fetchall()
                con.commit()
                con.close()
                return render_template('student_course_enrolment.html',data=data,data2=data2, idd = current_user.id,name= current_user.name,dataC=dataC)

@Timetable_lecturer.route('/download/report/pdf', methods=['GET', 'POST'])
def download_report():
    con = sqlite3.connect("instance/db.sqlite")
    cur = con.cursor()
    SEM = 223
    
    try:

  
        user_id = current_user.id


        cur.execute("SELECT * FROM TimeTablePDF where user_id = '%s' and SEM = '%s'" % (user_id, SEM))
        
        
        con.commit()

        result = cur.fetchall()
        cur.execute("SELECT sum(credit) as cc FROM TimeTablePDF where user_id = '%s' and SEM = '%s'" % (user_id, SEM))
        con.commit()

        credit = cur.fetchall()
        cur.execute("SELECT distinct name FROM TimeTablePDF where user_id = '%s' and SEM = '%s' " % (user_id, SEM))
        con.commit()

        name = cur.fetchall()
        pdf = FPDF()
        pdf.add_page()
         
        page_width = pdf.w - 2 * pdf.l_margin
         
        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Time Table', align='C')
        pdf.ln(10)
        th = pdf.font_size

        for row in name:
            pdf.set_font('Times','B',12.0) 
            pdf.cell(25, th, 'Name', border=1)
            pdf.set_font('Times','',12.0) 
            pdf.cell(95, th, row[0], border=1)
        pdf.ln(10)
 
        pdf.set_font('Times', 'B', 12)
         
        #col_width = page_width/4
         
        pdf.ln(1)
         
        
        pdf.cell(25, th, 'Code', border=1)
        pdf.cell(95, th, 'Name', border=1)
        pdf.cell(17, th, 'Credit', border=1)
        pdf.cell(22, th, 'Day', border=1)
        pdf.cell(15, th, 'From', border=1)
        pdf.cell(15, th, 'To', border=1)
        pdf.ln(th)
        pdf.set_font('Times', '', 12)
        th = pdf.font_size
        for row in result:
            #pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.cell(25, th, row[1], border=1)
            pdf.cell(95, th, row[2], border=1)
            pdf.cell(17, th, str(row[3]), border=1)
            pdf.cell(22, th, row[4], border=1)
            pdf.cell(15, th, str(row[5]), border=1)
            pdf.cell(15, th, str(row[6]), border=1)
            pdf.ln(th)
         
        pdf.ln(10)
        
        for row in credit:
            pdf.set_font('Times','B',12.0) 
            pdf.cell(25, th, 'Total Credit', border=1)
            pdf.set_font('Times','',12.0) 
            pdf.cell(15, th,str(row[0]), border=1)
        pdf.ln(10)

        pdf.set_font('Times','',10.0) 
        pdf.cell(page_width, 0.0, '- end of report -', align='C')
        
        return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename=timeTable_report.pdf'})
    except Exception as e:
        print(e)
    finally:
        cur.close() 
        con.close()