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
                
                user_id = current_user.id
                print(user_id)
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()
                cur.execute("SELECT default_sem FROM default_sem")
                SEM = cur.fetchone()[0]
                con.commit()
                cur.execute("SELECT * from lecturer_TimeTable where lec_id = '%s' and SEM = '%s'" % (user_id,SEM))
                data2 = cur.fetchall()
                cur.execute("SELECT sum(credit) FROM lecturer_TimeTable where lec_id = '%s' and SEM = '%s'" % (user_id, SEM))
                dataC = cur.fetchall()
                con.commit()
                con.close()
                return render_template('Timetable_lecturer.html',data2=data2, idd = current_user.id,name= current_user.name,dataC=dataC)

@Timetable_lecturer.route('/download/report/pdfsl', methods=['GET', 'POST'])
def download_report():
    
    
    try:

        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()
        cur.execute("SELECT default_sem FROM default_sem")
        SEM = cur.fetchone()[0]
        con.commit()
        user_id = current_user.id
        print('pdf')
        print(user_id)

        cur.execute("SELECT * from lecturer_TimeTable where lec_id = '%s' and SEM = '%s'" % (user_id,SEM))
        
        
        con.commit()

        result = cur.fetchall()
        cur.execute("SELECT sum(credit) FROM lecturer_TimeTable where lec_id = '%s' and SEM = '%s'" % (user_id, SEM))
        con.commit()

        credit = cur.fetchall()
        cur.execute("SELECT distinct name FROM lecturer_TimeTable where lec_id = '%s' and SEM = '%s' " % (user_id, SEM))
        con.commit()

        name = cur.fetchall()
        pdf = FPDF()
        pdf.add_page()
         
        page_width = pdf.w - 2 * pdf.l_margin
         
        pdf.set_font('Times','B',14.0) 
        for row in result:
            pdf.cell(page_width, 0.0, 'Time Table ' + row[8], align='C')
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
         
        
        pdf.cell(23, th, 'Code', border=1)
        pdf.cell(90, th, 'Name', border=1)
        pdf.cell(13, th, 'Credit', border=1)
        pdf.cell(22, th, 'Day', border=1)
        pdf.cell(13, th, 'From', border=1)
        pdf.cell(13, th, 'To', border=1)
        pdf.cell(17, th, 'Location', border=1)
        pdf.ln(th)
        pdf.set_font('Times', '', 12)
        th = pdf.font_size
        for row in result:
            #pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.cell(23, th, row[0], border=1)
            pdf.cell(90, th, row[1], border=1)
            pdf.cell(13, th, str(row[2]), border=1)
            pdf.cell(22, th, row[3], border=1)
            pdf.cell(13, th, str(row[4]), border=1)
            pdf.cell(13, th, str(row[5]), border=1)
            if row[6] is None:
                 pdf.cell(17, th, '', border=1)
            else:
                pdf.cell(17, th, row[6], border=1)
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
        
        return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename=lecturer5_TimeTable_report.pdf'})
    except Exception as e:
        print(e)
    finally:
        cur.close() 
        con.close()