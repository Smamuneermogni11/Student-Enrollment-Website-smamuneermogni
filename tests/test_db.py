import sqlite3

import pytest
from __init__ import db
from main import create_app





def test_saverloc():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/saverloc',
                                    data=dict(name_loc='Test H 700', cap='60'))
        response = test_client.get('/saverloc')
        assert response.status_code == 200

def test_del_loc():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/del_loc',
                                    data=dict(locid='10'))
        response = test_client.get('/del_loc')
        assert response.status_code == 200

def test_add_course():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
        response = test_client.post('/add_coursef',
                                    data=dict(CourseCode='CSC 250', CourseName='Information Technology',CourseDescription='Information Technology',Department='3',Plan='1',Level='1',Credit='4',Day='1',From='8:00',To='12:00',Semester='222'))
        response = test_client.get('/add_coursef')
        assert response.status_code == 200

def test_del_course():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
        response = test_client.post('/del_course',
                                    data=dict(CourseID='200'))
        response = test_client.get('/del_course')
        assert response.status_code == 200

def test_allocate_classroomf():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
        test_client.post('/allocate_classroomf',
                                data=dict(nolec=None,course_id=4,classroom=13))                      
        response = test_client.get('/allocate_classroomf')
        assert response.status_code == 200

def test_allocate_lecturerf():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
        test_client.post('/allocate_lecturerf',
                                data=dict(nolec=None,course_id=132,lec_id=15))                      
        response = test_client.get('/allocate_classroomf')
        assert response.status_code == 200