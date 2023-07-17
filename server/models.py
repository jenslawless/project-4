from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

from config import db

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)

    course_list = db.relationship('Course', secondary='enrollments', backref='students')

    serialize_rules = ("-course_list", "-courses.students", "-courses.assignments.students")

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("Invalid email address. Email must contain an '@' symbol.")
        if len(email) > 40:
                raise ValueError("Invalid email address. Email must be a maximum of 40 characters long.")
        return email

class Assignment(db.Model, SerializerMixin):
    __tablename__ = "assignments"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    grades = db.relationship('Grade', backref='assignment')

    serialize_rules = ("-course.students",)

class Course(db.Model, SerializerMixin):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    teacher = db.relationship('User', backref='courses')
    assignments = db.relationship('Assignment', backref='course')

class Grade(db.Model, SerializerMixin):
    __tablename__ = "grades"

    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    value = db.Column(db.Integer)

    student = db.relationship('User', backref='grades')

enrollments = db.Table('enrollments',
    db.Column('student_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))
)
    





