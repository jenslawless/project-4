#!/usr/bin/env python3
from flask import Flask, request, make_response
from flask_migrate import Migrate
from models import *
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

class Courses(Resource):
    def get(self):
        courses = Course.query.all()
        courses_dict = []
        for course in courses:
            courses_dict.append(course.to_dict())
        
        return make_response(courses_dict, 200)

api.add_resource(Courses, '/courses')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
