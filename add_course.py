from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import Flask
import sqlite3
import semester
add_course = Blueprint('add_course', __name__) 
app = Flask(__name__)

@add_course.route("/add_coursef",methods = ["POST","GET"])
def add_coursef():
    if request.method=='GET':
        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()
        cur.execute("SELECT * FROM courses_view")
        data6 = cur.fetchall()
        cur.execute("SELECT * FROM dep")
        Department = cur.fetchall()
        cur.execute("SELECT * FROM Day")
        Day = cur.fetchall()
        cur.execute("SELECT * FROM Time_list")
        From = cur.fetchall()
        cur.execute("SELECT * FROM Time_list")
        To = cur.fetchall()
        cur.execute("SELECT * FROM Semester")
        Semester = cur.fetchall()
        return render_template('add_course.html',data6=data6,Department=Department,Day=Day,From=From,To=To,Semester=Semester)
    else: 
                CourseCode = request.form["CourseCode"]
                CourseName = request.form["CourseName"]
                CourseDescription = request.form["CourseDescription"]
                Department = request.form["Department"]
                Plan = request.form["Plan"]
                Level = request.form["Level"]
                Credit = request.form["Credit"]
                Day = request.form["Day"]
                From = request.form["From"]
                To = request.form["To"]
                Semester = request.form["Semester"]
                
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()

                cur.execute(""" INSERT INTO course (
                       course_code,
                       course_name,
                       course_descr, 
                       dep_id,
                       plan_id,
                       level_id,
                       credit,
                       Day_id,
                       fromT,
                       toT,
                       SEM
                   )
                   VALUES (
                       ?,?,?,?,?,?,?,?,?,?,?
                   );
""",(CourseCode, CourseName,CourseDescription,Department,Plan,Level,Credit,Day,From,To,Semester))
                con.commit()
                cur.execute("SELECT * FROM courses_view")
                data6 = cur.fetchall()
                cur.execute("SELECT * FROM dep")
                Department = cur.fetchall()
                cur.execute("SELECT * FROM Day")
                Day = cur.fetchall()
                cur.execute("SELECT * FROM Time_list")
                From = cur.fetchall()
                cur.execute("SELECT * FROM Time_list")
                To = cur.fetchall()
                cur.execute("SELECT * FROM Semester")
                Semester = cur.fetchall()
    return render_template("add_course.html",data6=data6,Department=Department,Day=Day,Form=From,To=To,Semester=Semester)


@add_course.route("/del_course",methods = ["POST","GET"])
def del_course():
    if request.method=='GET':
        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()
        cur.execute("SELECT * FROM courses_view")
        data6 = cur.fetchall()
        cur.execute("SELECT * FROM dep")
        Department = cur.fetchall()
        cur.execute("SELECT * FROM Day")
        Day = cur.fetchall()
        cur.execute("SELECT * FROM Time_list")
        From = cur.fetchall()
        cur.execute("SELECT * FROM Time_list")
        To = cur.fetchall()
        cur.execute("SELECT * FROM Semester")
        Semester = cur.fetchall()
        return render_template('add_course.html',data6=data6,Department=Department,Day=Day,Form=From,To=To,Semester=Semester)
    else: 
                CourseID = request.form["CourseID"]
                
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()         
                cur.execute("DELETE FROM course WHERE course_id = '%s'  " % (CourseID))
                con.commit()
                cur.execute("SELECT * FROM courses_view")
                data6 = cur.fetchall()
                cur.execute("SELECT * FROM dep")
                Department = cur.fetchall()
                cur.execute("SELECT * FROM Day")
                Day = cur.fetchall()
                cur.execute("SELECT * FROM Time_list")
                From = cur.fetchall()
                cur.execute("SELECT * FROM Time_list")
                To = cur.fetchall()
                cur.execute("SELECT * FROM Semester")
                Semester = cur.fetchall()
    return render_template("add_course.html",data6=data6,Department=Department,Day=Day,Form=From,To=To,Semester=Semester)