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



# Instruction to Run the Website:
After downloding the files go to the dirctery then follow the instructions.
### For windows user:
1. python3 -m venv venv # create the venv
2. venv\scripts\activate.bat # activate venv
3. pip install -r requirements.txt  # install the requirements
4. python.exe -m pip install --upgrade pip # upgrade if needed
5. python main.py # run the website
6. From the Browser go to  http://127.0.0.1:5000  # Browser the website



### For MacOS and Linux user:
1. Open Any Terminal and run below command:
python -m venv venv
2. Activate the Virtual Environment:
For Linux Based OS Or Mac-OS.
pip3 install --upgrade pip
source venv/bin/activate
3. pip install -r requirements.txt
4. python main.py


## Testing the Website: 
### For windows: 
python -m pytest test.py

### For MacOS and Linux user: 
pytest test.py

