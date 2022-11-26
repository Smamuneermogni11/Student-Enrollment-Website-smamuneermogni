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
insert_course = Blueprint('student_course_enrolment', __name__)
app = Flask(__name__)

@insert_course.route('/incourse', methods=['GET', 'POST']) 
def incourse():
        #with app.app_context():
                print('ins1')
            #if request.method == 'POST':
                course_id = request.form.get('course_id')
                #eee = request.form.get('idd')
                user_id = request.form.get('iddv',type=int)
                #request.form['submit_button'] == 'Do Something':
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()
                #cur.execute("SELECT A.Day_id, A.FromT, A.ToT, A.user_id, A.course_id FROM Time_table AS A, Time_table AS B WHERE b.user_id = a.user_id AND b.Day_id = a.Day_id AND b.FromT>=a.FromT AND b.ToT<=a.ToT AND b.FromT<=a.FromT AND b.ToT>=a.ToT")
                cur.execute(""" SELECT distinct

    cp1.Day_id AS CP1_Day_id,
    cp1.course_id AS CP1_course_id,
    cp1.fromT AS CP1_fromT,
    cp1.toT AS CP1_toT,

    cp2.Day_id AS CP2_Day_id,
    cp2.course_id AS CP2_course_id,
    cp2.fromT AS CP2_fromT,
    cp2.toT AS CP2_toT
FROM 
    Time_table AS cp1
JOIN
    course AS cp2 
    ON cp1.course_id = cp2.course_id
    
      And (cp2.fromT >= cp1.fromT and cp2.fromT < cp1.toT AND cp2.day_id <> cp1.day_id)
      OR (cp2.toT > cp1.fromT and cp2.toT <= cp1.toT AND cp2.day_id <> cp1.day_id)
      OR (cp2.fromT <= cp1.fromT and cp2.toT >= cp1.toT AND cp2.day_id <> cp1.day_id)
      AND cp1.user_id = ?
      AND cp2.course_id = ? """, (user_id, course_id))
                entry = cur.fetchone()

                if entry is None:
                     cur.execute("insert into Time_table (user_id,course_id, Day_id, fromT, toT) values (?,?,(SELECT Day_id FROM course where course_id  = ?),(SELECT fromT FROM course where course_id  = ?),(SELECT toT FROM course where course_id  = ?))", (user_id, course_id,course_id,course_id,course_id) )
                     error = "The course has been added successfully."
                     #cour2 = ""
                else:
                    error = "There is a time conflict. Choose another course."
                    #id_tuple = tuple(entry[1])
                    #cur.execute("SELECT course_id, course_code, course_name FROM course WHERE course_id in {};".format(id_tuple))
                    #cour2 = cur.fetchall()
            
                #cur.execute("insert into Time_table (user_id,course_id, Day_id, fromT, toT) values (?,?,(SELECT Day_id FROM course where course_id  = ?),(SELECT fromT FROM course where course_id  = ?),(SELECT toT FROM course where course_id  = ?))", (user_id, course_id,course_id,course_id,course_id) )
                cur.close()
                con.commit()
                
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()      

                cur.execute("SELECT course_id, course_code, course_name, level_id, credit , Day_id , FromT, Tot FROM course p WHERE  NOT EXISTS (SELECT * FROM   Time_table od WHERE  p.course_id = od.course_id and od.user_id = '%s') AND dep_id = (select dep_id from user where id  = '%s') " % (user_id,user_id))
                data = cur.fetchall()
                
                cur.execute("SELECT course.course_id, course.course_code, course.course_name, course.credit, course.day_id ,course.fromT, course.toT FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (user_id))
                data2 = cur.fetchall()
                cur.execute("SELECT sum(course.credit) FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (user_id))
                dataC = cur.fetchall()
                
                con.commit()
                con.close()
              




                
                return render_template('student_course_enrolment.html',data=data,data2=data2, idd = current_user.id,name= current_user.name,dataC=dataC,error=error)


@insert_course.route('/delcourse', methods=['GET', 'POST']) 
def delcourse():
        #with app.app_context():
            
            #if request.method == 'POST':
                course_id = request.form.get('course_id_del')
                #eee = request.form.get('iddc')
                #user_id = request.form.get('iddc')
                user_id = request.form.get('iddc',type=int)
                #user_id = 1
                #request.form['submit_button'] == 'Do Something':
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()
                query = "DELETE FROM Time_table WHERE user_id = ? and course_id = ?"
                cur.execute(query,(user_id, course_id))
                con.commit()
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()      
                cur.execute("SELECT course_id, course_code, course_name, level_id, credit , Day_id , FromT, Tot FROM course p WHERE  NOT EXISTS (SELECT * FROM   Time_table od WHERE  p.course_id = od.course_id and od.user_id = '%s') AND dep_id = (select dep_id from user where id  = '%s' ) " % (user_id,user_id))
                #cur.execute("SELECT course_id,course_code,course_name,level_id,credit FROM course where dep_id = (select dep_id from user where id  = '%s' ) " % (user_id))
                data = cur.fetchall()
                
                cur.execute("SELECT course.course_id, course.course_code, course.course_name, course.credit, course.day_id ,course.fromT, course.toT FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (user_id))
                data2 = cur.fetchall()
                cur.execute("SELECT sum(course.credit) FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (user_id))
                dataC = cur.fetchall()
                con.commit()
                con.close()
                return render_template('student_course_enrolment.html',data=data,data2=data2, idd = current_user.id,name= current_user.name,dataC=dataC)
@insert_course.route('/download/report/pdf', methods=['GET', 'POST'])
def download_report():
    con = sqlite3.connect("instance/db.sqlite")
    cur = con.cursor()
    print('ins3')
    
    try:

  
        user_id = current_user.id


        cur.execute("SELECT * FROM TimeTablePDF where user_id = '%s'" % (user_id))
        
        
        con.commit()

        result = cur.fetchall()
        cur.execute("SELECT sum(credit) as cc FROM TimeTablePDF where user_id = '%s'" % (user_id))
        con.commit()

        credit = cur.fetchall()
        cur.execute("SELECT distinct name FROM TimeTablePDF where user_id = '%s'" % (user_id))
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