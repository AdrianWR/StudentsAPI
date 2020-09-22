#!/usr/bin/python3

import os
from flask import Flask
from flask import request, jsonify, json
from flask_pymongo import PyMongo
from werkzeug.exceptions import HTTPException

from models import Student
from error import InvalidUsage

# Initiate a new Flask application instance,
# connect it to Mongo DB driver and create 
# database connection variable

application = Flask(__name__)
application.config["DEBUG"] = os.environ.get("APP_DEBUG", False)
application.config["MONGO_URI"] = f"mongodb://{os.environ['MONGODB_USERNAME']}:{os.environ['MONGODB_PASSWORD']}@{os.environ['MONGODB_HOSTNAME']}:27017/{os.environ['MONGODB_DATABASE']}"

mongo = PyMongo(application)
db = mongo.db

###################
# GET Method -- / #
###################

@application.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to 42 API'})

###########################
# GET Method -- /students #
###########################

@application.route('/students', defaults={'id': None})
@application.route('/students/<int:id>')
def get_students(id):
    filter = { }
    if id is not None:
        filter['id'] = id
    if 'projects' in request.args:
        filter['projects'] = request.args['projects']
    students = [i for i in db.students.find(filter,{'_id': 0})] 
    if len(students) == 0:
        return jsonify(students), 204
    return jsonify(students), 200

###############
# POST Method #
###############

@application.route('/students', methods=['POST'])
def post_student():
    student = Student(request, db)
    db.students.insert_one(student())
    student().pop("_id")
    return jsonify(student()), 201

#################
# DELETE Method #
#################

@application.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    result = db.students.delete_one({'id': id})
    if (result.deleted_count == 0):
        raise InvalidUsage("Not Found", 404)
    return jsonify({}), 200

#######################
# HTTP Error Handlers #
#######################

@application.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response, response.status_code

@application.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({"message": e.name}), e.code


if __name__ == "__main__":
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 3000)
    application.run(host="0.0.0.0", port=ENVIRONMENT_PORT)
