from main import create_app
from flask_login import login_user, logout_user, login_required, current_user


def test_home_page_post():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Home Page Test" not in response.data

def test_home_page_get():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/')

        assert response.status_code == 200
        assert b"Home Page Test" not in response.data



def test_index():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Home Page Test" not in response.data

def test_About():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
        response = test_client.get('/About')
        assert response.status_code == 200
        assert b"About Page Test" not in response.data

def test_add_course():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
        response = test_client.get('/add_coursef')
        assert response.status_code == 200
        assert b"add course Page Test" not in response.data

def test_add_Loc():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/saverloc')
        assert response.status_code == 200
        assert b"Add calssRoom Page Test" not in response.data

# def test_admin_course_enrolment():
#     flask_app = create_app()
#     with flask_app.test_client() as test_client:
#         listx = [(None,)]
#         test_client.post('/login',
#                                 data=dict(email='naif.alblawi@admin.edu', password='123'))
#         test_client.post('/admin_course_enrolment',
#                                 data=dict(data=1,data2=1, idd = None,dataC=listx, dbstdi=1,current_Sem_Dec='Spring 2022'))                      
#         response = test_client.get('/admin_course_enrolment')
#         assert response.status_code == 200

def test_base():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
        test_client.post('/base',
                                data=dict(rol_id='1'))                      
        response = test_client.get('/base')
        assert response.status_code == 200

def test_Timetable_lecturerf():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
        test_client.post('/Timetable_lecturerf',
                                data=dict(data2= None, idd = 1 ,name='Naif',dataC=None))                      
        response = test_client.get('/Timetable_lecturerf')
        assert response.status_code == 200


def test_student_lists():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
                           
        response = test_client.get('/student_lists')
        assert response.status_code == 200

def test_student_lists_lecf():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
                           
        response = test_client.get('/student_lists_lec')
        assert response.status_code == 200

def test_Statsf():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='naif.alblawi@admin.edu', password='123'))
                           
        response = test_client.get('/Stats')
        assert response.status_code == 200

def test_StatsSTDf():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='yousef@std.csc', password='123'))
                           
        response = test_client.get('/StatsSTD')
        assert response.status_code == 200

def test_download_report():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        test_client.post('/login',
                                data=dict(email='Dez@lec.phys', password='123'))
                           
        response = test_client.get('/download/report/pdfsl')
        assert response.status_code == 200