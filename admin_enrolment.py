import email
import sqlite3
from this import s
from types import NoneType
from flask import Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash,session
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


admin_enrolment = Blueprint('admin_enrolment', __name__)
app = Flask(__name__)

@admin_enrolment.route('/admin_course_enrolment/', methods=['GET', 'POST'])
def adstudent():
    with app.app_context():
            #user_id = request.form.get('stdid')
            session['my_var'] = request.form.get('stdid')
            user_id =  session.get('my_var', None)
            print('a1') 
            con = sqlite3.connect("instance/db.sqlite")
            cur = con.cursor()      
        
            cur.execute("SELECT id, name FROM user WHERE id = '%s'" % (user_id))
        
            dbstdi = cur.fetchall()
            cur.execute("SELECT course_id, course_code, course_name, level_id, credit, Day_id , FromT, Tot FROM course p WHERE  NOT EXISTS (SELECT * FROM   Time_table od WHERE  p.course_id = od.course_id and od.user_id = '%s') AND dep_id = (select dep_id from user where id  = '%s' )" % (user_id,user_id))
            data = cur.fetchall()
            cur.execute("SELECT course.course_id, course.course_code, course.course_name, course.credit,course.day_id ,course.fromT, course.toT FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (user_id))
            data2 = cur.fetchall()
            cur.execute("SELECT sum(course.credit) FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (user_id))
            dataC = cur.fetchall()
            con.commit()
            con.close()
            print('a2')
    return render_template('admin_course_enrolment.html',data=data,data2=data2, idd = user_id,name= current_user.name,dataC=dataC, dbstdi=dbstdi)

@admin_enrolment.route('/admin_incourse', methods=['GET', 'POST']) 
def adincourse():
        #with app.app_context():
                print('a3')
            #if request.method == 'POST':
                course_id = request.form.get('course_id')
                #eee = request.form.get('idd')
                user_id =  session.get('my_var', None)
                user_info = session.get('my_var')
                #request.form['submit_button'] == 'Do Something':
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()
                cur.execute("SELECT id, name FROM user WHERE id = '%s'" % (user_id))
        
                dbstdi = cur.fetchall()
                #cur.execute("insert into Time_table (user_id,course_id) values (?,?)", (user_id, course_id) )
                #cur.execute("INSERT INTO Time_table(user_id,course_id) SELECT ?, ? WHERE NOT EXISTS(SELECT 1 FROM Time_table WHERE user_id = ? AND course_id = ?)", (user_id, course_id,user_id, course_id))
                #con.commit()
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
    
      And (cp2.fromT >= cp1.fromT and cp2.fromT < cp1.toT)
      OR (cp2.toT > cp1.fromT and cp2.toT <= cp1.toT)
      OR (cp2.fromT <= cp1.fromT and cp2.toT >= cp1.toT)
      and cp2.day_id = cp1.day_id
      AND cp1.user_id = ?
      AND cp2.course_id = ? """, (user_id, course_id))
                entry = cur.fetchone()

                if entry is None:
                     cur.execute("insert into Time_table (user_id,course_id, Day_id, fromT, toT) values (?,?,(SELECT Day_id FROM course where course_id  = ?),(SELECT fromT FROM course where course_id  = ?),(SELECT toT FROM course where course_id  = ?))", (user_id, course_id,course_id,course_id,course_id) )
                     error = "Course ADD"
                     #cour2 = ""
                else:
                    error = "Time Conflict"
                    #id_tuple = tuple(entry[1])
                    #cur.execute("SELECT course_id, course_code, course_name FROM course WHERE course_id in {};".format(id_tuple))
                    #cour2 = cur.fetchall()
            
                #cur.execute("insert into Time_table (user_id,course_id, Day_id, fromT, toT) values (?,?,(SELECT Day_id FROM course where course_id  = ?),(SELECT fromT FROM course where course_id  = ?),(SELECT toT FROM course where course_id  = ?))", (user_id, course_id,course_id,course_id,course_id) )
                cur.close()
                con.commit()


                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()      

                cur.execute("SELECT course_id, course_code, course_name, level_id, credit, Day_id , FromT, Tot FROM course p WHERE  NOT EXISTS (SELECT * FROM   Time_table od WHERE  p.course_id = od.course_id and od.user_id = '%s') AND dep_id = (select dep_id from user where id  = '%s') " % (user_id,user_id))
                data = cur.fetchall()
                
                cur.execute("SELECT course.course_id, course.course_code, course.course_name, course.credit, course.day_id ,course.fromT, course.toT FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (user_id))
                data2 = cur.fetchall()
                cur.execute("SELECT sum(course.credit) FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (user_id))
                dataC = cur.fetchall()
                
                con.commit()
                con.close()
              




                
                return render_template('admin_course_enrolment.html',data=data,data2=data2, idd = user_id,name= current_user.name,dataC=dataC, dbstdi=dbstdi,error=error)


@admin_enrolment.route('/admin_delcourse', methods=['GET', 'POST']) 
def addelcourse():
        #with app.app_context():
            
            #if request.method == 'POST':
                course_id = request.form.get('course_id_del')
                #eee = request.form.get('iddc')
                #user_id = request.form.get('iddc')
                user_id = session.get('my_var', None)
                user_info = session.get('my_var')
                #user_id = 1
                #request.form['submit_button'] == 'Do Something':
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()
                query = "DELETE FROM Time_table WHERE user_id = ? and course_id = ?"
                cur.execute(query,(user_id, course_id))
                con.commit()
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()      
                cur.execute("SELECT course_id, course_code, course_name, level_id, credit, Day_id , FromT, Tot FROM course p WHERE  NOT EXISTS (SELECT * FROM   Time_table od WHERE  p.course_id = od.course_id and od.user_id = '%s') AND dep_id = (select dep_id from user where id  = '%s' ) " % (user_id,user_id))
                #cur.execute("SELECT course_id,course_code,course_name,level_id,credit FROM course where dep_id = (select dep_id from user where id  = '%s' ) " % (user_id))
                data = cur.fetchall()
                cur.execute("SELECT id, name FROM user WHERE id = '%s'" % (user_id))
        
                dbstdi = cur.fetchall()
                cur.execute("SELECT course.course_id, course.course_code, course.course_name, course.credit, course.day_id ,course.fromT, course.toT FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (user_id))
                data2 = cur.fetchall()
                cur.execute("SELECT sum(course.credit) FROM course INNER JOIN Time_table ON course.course_id =Time_table.course_id where Time_table.user_id = '%s'" % (user_id))
                dataC = cur.fetchall()
                con.commit()
                con.close()
                return render_template('admin_course_enrolment.html',data=data,data2=data2, idd = user_id,name= current_user.name,dataC=dataC, dbstdi=dbstdi)