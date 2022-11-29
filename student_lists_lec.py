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
student_lists_lec = Blueprint('student_lists_lec', __name__)
app = Flask(__name__)

@student_lists_lec.route('/student_lists_lec', methods=['GET', 'POST']) 
def student_lists_lecf():
                SEM = 223
                user_id = current_user.id
                print(user_id)
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()
                
                cur.execute("SELECT * from student_list where lec_id = '%s' and sem_id = '%s'" % (user_id,SEM))
                data2 = cur.fetchall()

                con.commit()
                con.close()
                return render_template('student_lists_lec.html',data2=data2, idd = current_user.id,name= current_user.name)

@student_lists_lec.route('/download/report/pdfslec', methods=['GET', 'POST'])
def download_report():
    
    
    try:

        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()
        SEM = 223
        user_id = current_user.id
        print(user_id)

        cur.execute("SELECT * from student_list where lec_id = '%s' and sem_id = '%s'" % (user_id,SEM))
        
        
        con.commit()

        result = cur.fetchall()
    
        pdf = FPDF(orientation="landscape", format="A4")
        pdf.add_page()
      






         
        page_width = pdf.w - 2 * pdf.l_margin
         
        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Student List', align='C')
        pdf.ln(10)
        th = pdf.font_size

        pdf.ln(10)
 
        pdf.set_font('Times', 'B', 12)
         
        #col_width = page_width/4
         
        pdf.ln(1)
         
        
        pdf.cell(8, th, 'ID', border=1, align='C')
        pdf.cell(25, th, 'Name', border=1, align='C')
        pdf.cell(15, th, 'Dep', border=1, align='C')
        pdf.cell(22, th, 'Code', border=1, align='C')
        pdf.cell(65, th, 'Course Name', border=1, align='C')
        pdf.cell(22, th, 'Day', border=1, align='C')
        pdf.cell(11, th, 'From', border=1, align='C')
        pdf.cell(11, th, 'To', border=1, align='C')
        pdf.cell(25, th, 'Semester', border=1, align='C')
        pdf.ln(th)
        pdf.set_font('Times', '', 12)
        th = pdf.font_size
        for row in result:
            #pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.cell(8, th, str(row[0]), border=1, align='C')
            pdf.cell(25, th, row[1], border=1, align='C')
            pdf.cell(15, th, row[2], border=1, align='C')
            pdf.cell(22, th, row[3], border=1, align='C')
            pdf.cell(65, th, row[4], border=1, align='C')
            pdf.cell(22, th, row[5], border=1, align='C')
            pdf.cell(11, th, str(row[6]), border=1, align='C')
            pdf.cell(11, th, str(row[7]), border=1, align='C')
            pdf.cell(25, th, row[8], border=1, align='C')
            pdf.ln(th)
         
        pdf.ln(10)
        
     

        pdf.set_font('Times','',10.0) 
        pdf.cell(page_width, 0.0, '- end of report -', align='C')
        
        return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename=Student_List_lec_report.pdf'})
    except Exception as e:
        print(e)
    finally:
        cur.close() 
        con.close()