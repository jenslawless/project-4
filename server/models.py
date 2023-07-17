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

@validates('email')
def validate_email(self, key, email):
    if '@' not in email:
        raise ValueError("Invalid email address. Email must contain an '@' symbol.")
    if len(email) > 40:
            raise ValueError("Invalid email address. Email must be a maximum of 40 characters long.")
    return email

class StudentCourse(db.Model, SerializerMixin):
    __tablename__ = "students_courses"

    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

class Assignment(db.Model, SerializerMixin):
    __tablename__ = "assignments"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    grade = db.Column(db.Integer)


    student = db.relationship('User', backref='assignments')
    course = db.relationship('Course', backref='assignments')


class Course(db.Model, SerializerMixin):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    teacher = db.relationship('User', backref=('courses'))
    students_courses = db.relationship('StudentCourse', backref='course')





