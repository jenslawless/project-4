#!/usr/bin/env python3

# Standard library imports
from random import random, randint, sample, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import *

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

def seed_assignments(courses, users):
    assignments = []
    student_users = [user for user in users if user.role == 'student']


    for course in courses:
        num_assignments = randint(4, 7)

        for _ in range(num_assignments):
            new_assignment = Assignment(
                description=fake.sentence(),
                course_id=course.id,
            )
            assignments.append(new_assignment)

    return assignments


def seed_grades(assignments):
    grades = []

    for assignment in assignments:
        course = assignment.course
        students = course.students  # Retrieve the enrolled students for the course

        for student in students:
            grade = Grade(
                assignment_id=assignment.id,
                student_id=student.id,
                value=randint(60, 100)
            )
            grades.append(grade)

    return grades

if __name__ == '__main__':

    with app.app_context():
        print("Clearing db...")
        Course.query.delete()
        Assignment.query.delete()
        Grade.query.delete()
        User.query.delete()
        enrollments.delete()

        print("Seeding users...")
        users = seed_users()
        db.session.add_all(users)
        db.session.commit()

        print("Seeding courses...")
        courses = seed_courses(users)
        db.session.add_all(courses)
        db.session.commit()

        print("Seeding assignments...")
        assignments = seed_assignments(courses, users)
        db.session.add_all(assignments)
        db.session.commit()

        print("Seeding grades...")
        grades = seed_grades(assignments)
        db.session.add_all(grades)
        db.session.commit()

        print("Done seeding!")
