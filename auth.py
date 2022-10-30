
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_login import login_user, logout_user, login_required, current_user
from __init__ import create_app, db
from flask import Flask
import sqlite3
auth = Blueprint('auth', __name__) 
app = Flask(__name__)
with app.app_context():
    con = sqlite3.connect("instance/db.sqlite")

    cur = con.cursor()


    cur.execute("SELECT * FROM dep")
    data = cur.fetchall()

    con.close()
@auth.route("/saverecord",methods = ["POST","GET"])
def saveRecord():
    if request.method=='GET':
        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()
        cur.execute("SELECT * FROM lec")
        data6 = cur.fetchall()
        return render_template('add_lec.html',data6=data6)
    else: 
                name = request.form["name"]
                email = request.form["email"]
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()

                cur.execute("INSERT into lec (lec_name, lec_email) values (?,?)",(name, email))
                con.commit()
                cur.execute("SELECT * FROM lec")
                data6 = cur.fetchall()
    return render_template("add_lec.html",data6=data6)

@auth.route("/saverloc",methods = ["POST","GET"])
def saverloc():
    if request.method=='GET':
        con = sqlite3.connect("instance/db.sqlite")
        cur = con.cursor()
        cur.execute("SELECT * FROM loc")
        data6 = cur.fetchall()
        return render_template('add_loc.html',data6=data6)
    else: 
                name_loc = request.form["name_loc"]
                cap = request.form["cap"]
                con = sqlite3.connect("instance/db.sqlite")
                cur = con.cursor()

                cur.execute("INSERT into loc (loc_name, loc_Cap) values (?,?)",(name_loc, cap))
                con.commit()
                cur.execute("SELECT * FROM loc")
                data6 = cur.fetchall()
    return render_template("add_loc.html",data6=data6)

#cursor.execute("INSERT into lec (name, email) values (?,?)",(name, email))
@auth.route('/login', methods=['GET', 'POST']) 
def login(): 
    if request.method=='GET': 
        return render_template('login.html')
    else: 
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=email).first()
    

        if not user:
            flash('Please sign up before!')
            return redirect(url_for('auth.signup'))
        elif not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) 
            
        login_user(user, remember=remember)
        return redirect(url_for('main.profile'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup(): 
    if request.method=='GET': 
        
        return render_template('signup.html', data=data)
    else: 
        email = request.form.get('email')
        name = request.form.get('name')
        dep_id = request.form.get('dep_id')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first() 
        if user: 
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))
        
        new_user = User(email=email, name=name, dep_id=dep_id, password=generate_password_hash(password, method='sha256')) #
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))


@auth.route('/logout') 
@login_required
def logout(): 
    logout_user()
    return redirect(url_for('main.index'))