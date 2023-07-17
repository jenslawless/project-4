#!/usr/bin/env python3

# Standard library imports
from random import random, randint, sample, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, StudentCourse, Assignment, Course

fake = Faker()

def seed_users():
    users = []
    for _ in range(100):
        role_probability = random()

        if role_probability <= 0.25:
            role = 'teacher'
        else:
            role = 'student'

        user = User(
            name=fake.name(),
            email=fake.email(),
            password=fake.password(),
            role=role
        )
        users.append(user)

    return users

def seed_courses(users):
    courses = ["Algebra", "Physics", "English", "US History", "Ceramics", "Chemistry", "Art History"]
    course_list = []
    teacher_ids = [user for user in users if user.role == 'teacher']

    for course in courses:
        c = Course(
            name=course,
            description=fake.text(),
            teacher_id=rc(teacher_ids).id
        )
        course_list.append(c)
    
    return course_list

def seed_studentcourse(users, courses):
    studentcourses = []
    student_users = [user for user in users if user.role == 'student']
    
    for user in student_users:
        num_courses = randint(2, 5)
        user_courses = sample(courses, num_courses)

        for course in user_courses:
            studentcourse = StudentCourse(
                student_id=user.id,
                course_id=course.id
            )
        
            studentcourses.append(studentcourse)
    
    return studentcourses

def seed_assignments(courses, users):
    assignments = []
    student_users = [user for user in users if user.role == 'student']

    for course in courses: 
        enrolled_students = [user for user in student_users if course in user.course_list]
        
        for _ in range(4, 7):       
            new_assignment = Assignment(
                description=fake.sentence(),
                course_id=course.id,
                grade=rc(range(60, 100))
            )
            assignments.append(new_assignment)

    return assignments

if __name__ == '__main__':

    with app.app_context():
        print("Clearing db...")
        Course.query.delete()
        Assignment.query.delete()
        StudentCourse.query.delete()
        User.query.delete()

        print("Seeding users...")
        users = seed_users()
        db.session.add_all(users)
        db.session.commit()

        print("Seeding courses...")
        courses = seed_courses(users)
        db.session.add_all(courses)
        db.session.commit()

        print("Seeding student courses...")
        studentcourses = seed_studentcourse(users, courses)
        db.session.add_all(studentcourses)
        db.session.commit()

        print("Seeding assignments...")
        assignments = seed_assignments(courses, users)
        db.session.add_all(assignments)
        db.session.commit()

        print("Done seeding!")
