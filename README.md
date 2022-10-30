# **PythonByte**   
## IST303-Group-Project    
## **Team members:** 
KRISTINA, NAIF, MUNEER, DESMEND       

## **Team name: PythonByte**   

## **Development Environment:**
**Frontend:** HTML, CSS, Bootstrap , Javascript   
**Backend:** Python 3.10, Flask Web Framework, Virtual Environment , Microsoft Sql Server Database    


## **Product:**
Student Enrollment System Website   

## **Project Description:**

The Website is designed to serve educational organizations that will allow students to enroll in courses, with features such as printing several reports (timetable, location, courses, student list), implemented academic calendar, future course plans, and statical information. The organization will have control over the website with multiple rolls such as managers, lectures, and staff, each with their special features from printing reports to updating the data. 
The main objective is to construct a system that allows students to plan efficiently when enrolling in courses and have a better perspective of the requirement and the timeframe to finish their degree. The website will provide guidelines and alternative course plans. 

  
  
## **Stakeholders:**
Lecturers, Students, Regustration Staff Members, Regustration Managers, Head Officials   
    
## **Decomposed User Stories into Tasks and Allocate tasks to each team member and record the allocation:**  
 [Link](https://github.com/Smamuneermogni11/PythonByte/blob/dbd955c6568bd190501809b20042b123f04677fa/User%20Stories%20broken%20into%20Tasks%20with%20Team%20Member%20Allocated.pdf)       

## Features in Milestone 1: 

Backend: Database Backbone (Create Tables, Users Table and rols)  

Frontend: Web Page (Main: login page ,Student: Enrolment, Student: Courses Plan, Student: future Courses Plan, Lecturer: Timetable, Lecturer: Student Lists)

## 2 Iterations for Milestone 1 (4 weeks):
Iteration 1 (2 weeks): 

1. Develop Database Design 

2. Create Flask Project and Venv 

3. Create Database.	 

Iteration 2 (2 weeks): 

1. Create Template and Style.  

2. Create Webpage: (Main: login page ,Student: Enrolment, Student: Courses Plan, Student: future Courses Plan, Lecturer: Timetable, Lecturer: Student Lists) 

## Calculate Velocity:

Timeline: 4 weeks to milestone 1, 5 weeks to milestone 2

Iteration 1: 3 user stories x 8 story points = 24
Iteration 2: 7 user stories x 8 story points = 56

Total = 80

So, your average velocity is 80 ÷ 2 = 40.

Starting velocity: 40 %
Total: 6 hours per week
Current: 4 hours per week


# Burn Down Chart:

[Link](https://cgu0-my.sharepoint.com/:x:/g/personal/naif_alblawi_cgu_edu/EbCUGVcGgQhFhw6ms9QRkyoBjbVyxxy0AC-dhmHFM0yjsQ?e=fc0rfN)

# Stand Up Meeting:

[Link](https://cgu0-my.sharepoint.com/:w:/g/personal/naif_alblawi_cgu_edu/ETbM1UMhSCBIk1TWXlAk8RgB1zL2sjUGkMI1gdLABZNXiQ?e=b1Bibx)

# Instructions for Visual Studio Code:

# Instruction to virtual environment:

### For windows user:
1.C:\> pip install virtualenv

2. venv\Scripts\activate.bat

3. python -m pip install --upgrade pip

4. python -m pip install flask
  
    paste this code in visual studio code
    
    Then run this code in terminal:

python -m flask run

When renamed the flask file: set Flask_APP=front_page

After getting the website link:
### Output:
Hold Ctrl button and click on the link:

(venv) C:\Users\Muneer\Desktop\work>python -m flask run
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [01/Oct/2022 16:01:51] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Oct/2022 16:01:51] "GET /favicon.ico HTTP/1.1" 404 -


### For MacOS and Linux user:
1. Open Any Terminal and run below command:
python -m venv venv
2. Activate the Virtual Environment:
For Linux Based OS Or Mac-OS.
pip3 install --upgrade pip
source venv/bin/activate
3. Installing Flask:
pip install -U Flask

4. Flask run


# Testing the web page: 
For windows: 
$ pip install pytest
from front_page import app

def test_front_page():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'PythonByte!'
  For MacOS and Linux:
  pip3 install pytest
  
    
    
## To run the test:
For windows: 
pytest test_front_page.py

Output:
(venv) C:\Users\Muneer\Desktop\work>pytest test_front_page.py
========================================================== test session starts ===========================================================
platform win32 -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
rootdir: C:\Users\Muneer\Desktop\work
collected 1 item

test_front_page.py .                                                                                                                [100%]

For MacOS and Linux: 
pytest test_front_page.py
