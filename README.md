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

Backend: Database Backbone (Create Tables, Users Table and roles)  

Frontend: Web Page (Main: login page , Sginup page, Student: Enrolment, Student: Avalible Courses , Add Lecturer: , Add ClassRoom)

## There are two Iterations for Milestone 1 (Total: 4 weeks):
Iteration 1 (2 weeks): 

1. Develop Database Design 

2. Create Flask Project and Venv 

3. Create Database.	 

Iteration 2 (2 weeks): 

1. Create Template and Style.  

2. Create Webpage: (Main: login page ,Student: Enrolment, Student: Courses Plan, Student: future Courses Plan, Lecturer: Timetable, Lecturer: Student Lists) 

## Calculate Velocity for Milestone 1:

Timeline: 4 weeks to milestone 1

Iteration 1: 3 user stories x 8 story points = 24
Iteration 2: 7 user stories x 8 story points = 56

Total = 80

So, your average velocity is 80 ÷ 2 = 40.

Starting velocity: 40 %
Total: 6 hours per week
Current: 4 hours per week

## Features in Milestone 2: 
Backend: course information, drop and select courses, course plan, future course plan, student timetable, lecturer time table, student semester plan, student list in specific registered course, course information, select student by id, students available course, enroll student list, drop a student,  course information (location, time, lecturer, and student count), staff course information, update course information, student list who did not enroll, enrolled student list, student list by course and semester, student individual timetable list, location by semester, time conflicts on locations, courses and teachers, student counts for enrolled, withdraw and dropout list, student count list comparison between current and previous semester, update calender, authenticate username and password for users.  

Frontent: Manager: Report print, Manager: Time conflict check button, Staff: Student report button (student id), Staff: Student Report button(semester wise search and print mode), Staff: Edit course(print button), Staff: Student enrollment button, Staff: Course information, Lecturer: student list button, Lecturer: Timetable button, Student: course plan print, Student: future course plan, Student: Enrollment button.

## There are two Iterations for Milestone 2 (Total: 9 weeks):

Iteration 1: (4 weeks)

1. Student can view available courses

2. Students have the ability to add or drop courses

3. Students have the ability to print Timetable

4. Registration staff members have the ability to drop or enroll students in the course

5. Staff members can change location, time and lecturer for specific course

6. Registration manager can check time conflict between locations, courses, students and lecturers.

Iteration 2: (5 weeks)

1. Student: Course plan and how current course plan will affect future course enrollment

2. Lecturer ability to print time table 

3. Lecturer ability to print student list 

4. Registration staff members ability to see student in each course with course information

5. Registration staff members ability to check students who are not enrolled in any course within time frame

6. Registration staff members ability to print reports such as student list, timetables, location and indivdual student timetable and teachers

7. Registration manager ability to print reports and statistics to compare between current and previous semester regarding student enrollment and dropouts

8.  Registration manager ability to organize calendar for registration tasks.

## Calculate Velocity for Milestone 2:

Timeline: 4 weeks to Iteration 1, 5 weeks to Iteration 2

Iteration 1: 6 user stories x 8 story points = 48
Iteration 2: 8 user stories x 8 story points = 64

Total = 112

So, your average velocity is 112 ÷ 2 = 40.

Starting velocity: 56 %
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
