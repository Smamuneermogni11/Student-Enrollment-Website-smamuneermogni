from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_bootstrap import Bootstrap
db = SQLAlchemy()
def create_app():
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    db.init_app(app)
    #Bootstrap(app)
    login_manager = LoginManager() 
    login_manager.login_view = 'auth.login' 
    login_manager.init_app(app) 
    from models import User
    @login_manager.user_loader
    def load_user(user_id): 
        return User.query.get(int(user_id))
   
    
   
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from available_courses import available_courses as main_blueprint
    app.register_blueprint(main_blueprint)

    from insert_course import insert_course as main_blueprint
    app.register_blueprint(main_blueprint)

    from admin_enrolment import admin_enrolment as main_blueprint
    app.register_blueprint(main_blueprint)

    from allocate_classroom import allocate_classroom as main_blueprint
    app.register_blueprint(main_blueprint)

    from allocate_lecturer import allocate_lecturer as main_blueprint
    app.register_blueprint(main_blueprint)

    from add_course import add_course as main_blueprint
    app.register_blueprint(main_blueprint)

    from Timetable_lecturer import Timetable_lecturer as main_blueprint
    app.register_blueprint(main_blueprint)

    from student_lists import student_lists as main_blueprint
    app.register_blueprint(main_blueprint)
    
    

    return app