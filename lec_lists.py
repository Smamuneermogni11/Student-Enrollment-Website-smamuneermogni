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

lec_lists = Blueprint('lec_lists', __name__)
app = Flask(__name__)

@lec_lists.route('/lec_lists', methods=['GET', 'POST']) 
def lec_listsf():
                
                user_id = current_user.id
              
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()
                
                cur.execute("SELECT * from lec_lists ")
                data2 = cur.fetchall()

                con.commit()
                con.close()
                return render_template('lec_lists.html',data2=data2, idd = current_user.id,name= current_user.name)

@lec_lists.route('/download/report/pdfslecl', methods=['GET', 'POST'])
def download_report():
    
    
    try:

        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()
        
        user_id = current_user.id
        print(user_id)

        cur.execute("SELECT * from lec_lists")
        
        
        con.commit()

        result = cur.fetchall()
    
        pdf = FPDF(orientation="landscape", format="A4")
        pdf.add_page()
      






         
        page_width = pdf.w - 2 * pdf.l_margin
         
        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Lecturer List', align='C')
        pdf.ln(10)
        th = pdf.font_size

        pdf.ln(10)
 
        pdf.set_font('Times', 'B', 12)
         
        #col_width = page_width/4
         
        pdf.ln(1)
         
        
        pdf.cell(8, th, 'ID', border=1, align='C')
        pdf.cell(75, th, 'Name', border=1, align='C')
        pdf.cell(50, th, 'Dep', border=1, align='C')
       
        pdf.ln(th)
        pdf.set_font('Times', '', 12)
        th = pdf.font_size
        for row in result:
            #pdf.cell(col_width, th, str(row[0]), border=1)
            pdf.cell(8, th, str(row[0]), border=1, align='C')
            pdf.cell(75, th, row[1], border=1, align='C')
            pdf.cell(50, th, row[2], border=1, align='C')
            pdf.ln(th)
         
        pdf.ln(10)
        
     

        pdf.set_font('Times','',10.0) 
        pdf.cell(page_width, 0.0, '- end of report -', align='C')
        
        return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename=lec_List_report.pdf'})
    except Exception as e:
        print(e)
    finally:
        cur.close() 
        con.close()