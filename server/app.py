#!/usr/bin/env python3
from flask import Flask, request, make_response
from flask_migrate import Migrate
from models import db, User, Course, StudentCourse, Assignment
import os
from flask_restful import Api, Resource

# from config import app, db, api


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/')
def index():
    return '<h1>Phase 4 Project</h1>'

@app.route('/add_items')
def add_items():
    # Create instances of your model classes
    db.drop_all()
    db.create_all()

    teacher1 = User(name='Teacher 1', email='teacher1@example.com', password='password123', role='teacher')
    teacher2 = User(name='Teacher 2', email='teacher2@example.com', password='password456', role='teacher')
    teacher3 = User(name='Teacher 3', email='teacher3@example.com', password='password789', role='teacher')

    student1 = User(name='Student 1', email='student1@example.com', password='password123', role='student')
    student2 = User(name='Student 2', email='student2@example.com', password='password456', role='student')
    student3 = User(name='Student 3', email='student3@example.com', password='password789', role='student')
    student4 = User(name='Student 4', email='student4@example.com', password='password123', role='student')
    student5 = User(name='Student 5', email='student5@example.com', password='password456', role='student')
    student6 = User(name='Student 6', email='student6@example.com', password='password789', role='student')
    student7 = User(name='Student 7', email='student7@example.com', password='password123', role='student')
    student8 = User(name='Student 8', email='student8@example.com', password='password456', role='student')
    student9 = User(name='Student 9', email='student9@example.com', password='password789', role='student')
    student10 = User(name='Student 10', email='student10@example.com', password='password123', role='student')

    course1 = Course(name='Mathematics', description='Introduction to Calculus', teacher=teacher1)
    course2 = Course(name='History', description='World History', teacher=teacher2)
    course3 = Course(name='Physics', description='Introduction to Physics', teacher=teacher3)

    assignment1 = Assignment(description='Calculus Homework', student=student1, course=course1, grade=85)
    assignment2 = Assignment(description='World History Essay', student=student2, course=course2, grade=92)

    # Add the instances to the session and commit the changes
    db.session.add_all([teacher1, teacher2, teacher3, student1, student2, student3, student4, student5,
                        student6, student7, student8, student9, student10, course1, course2, course3,
                        assignment1, assignment2])
    db.session.commit()

    # Assign students to courses
    student_course1 = StudentCourse(student_id=student1.id, course_id=course1.id)
    student_course2 = StudentCourse(student_id=student2.id, course_id=course2.id)
    student_course3 = StudentCourse(student_id=student3.id, course_id=course3.id)
    student_course4 = StudentCourse(student_id=student4.id, course_id=course1.id)
    student_course5 = StudentCourse(student_id=student5.id, course_id=course2.id)
    student_course6 = StudentCourse(student_id=student6.id, course_id=course3.id)
    student_course7 = StudentCourse(student_id=student7.id, course_id=course1.id)
    student_course8 = StudentCourse(student_id=student8.id, course_id=course2.id)
    student_course9 = StudentCourse(student_id=student9.id, course_id=course3.id)
    student_course10 = StudentCourse(student_id=student10.id, course_id=course1.id)

    db.session.add_all([student_course1, student_course2, student_course3, student_course4,
                        student_course5, student_course6, student_course7, student_course8,
                        student_course9, student_course10])
    db.session.commit()

    return 'Items added successfully!'

@app.route('/users')
def get_users():
    students_courses = StudentCourse.query.all()

    # Display user information
    for user in students_courses:
        print(f"Name: {user.user.name}, Email: {user.user.email}")
        print(f"Course: {user.course.name}")

    return 'User information displayed in the console.'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
