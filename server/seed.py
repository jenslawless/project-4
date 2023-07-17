#!/usr/bin/env python3

# Standard library imports
from random import random, randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, StudentCourse, Assignment, Course

fake = Faker()


def seed_users(num_users):
    for _ in range(num_users):
        user = User(
            name=fake.name(),
            email=fake.email(),
            password=fake.password()
        )
        db.session.add(user)

    db.session.commit()

def seed_assignments(courses, users):
    assignments = []
    for _ in range(20):
        assignment = Assignment(
            description=fake.sentence(),
            student_id=random.choice([user.id for user in users]),
            course_id=random.choice([course.id for course in courses]),
            grade=random.choice(range(100))
        )
        assignments.append(assignment)
    return assignments

def seed_studentcourse(users, courses):
    studentcourses = []
    for _ in range(10):
        studentcourse = StudentCourse(
            student_id=random.choice([user.id for user in users]),
            course_id=random.choice([course.id for course in courses])
        )
        studentcourses.append(studentcourse)
    return studentcourses

def seed_courses(num_courses):

    teacher_ids = db.session.query(User.id).all()

    for _ in range(num_courses):
        course = Course(
            name=fake.name(),
            description=fake.text(),
            teacher_id=fake.random_element(teacher_ids)[0]
        )
        db.session.add(course)

    db.session.commit()

if __name__ == '__main__':

    with app.app_context():
        print("Clearing db...")
        Course.query.delete()
        Assignment.query.delete()
        StudentCourse.query.delete()
        User.query.delete()

        print("Seeding users...")
        seed_users(10)

        print("Seeding courses...")
        seed_courses(5)

        courses = Course.query.all()
        users = User.query.all()

        print("Seeding assignments...")
        assignments = seed_assignments(courses, users)
        db.session.add_all(assignments)
        db.session.commit()

        print("Seeding student courses...")
        studentcourses = seed_studentcourse(users, courses)
        db.session.add_all(studentcourses)
        db.session.commit()

        print("Done seeding!")
