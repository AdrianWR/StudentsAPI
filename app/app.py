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
    """Display home URL welcome message"""
    return jsonify({'message': 'Welcome to 42 API'})

###########################
# GET Method -- /students #
###########################

@application.route('/students', defaults={'id': None})
@application.route('/students/<int:id>')
def get_students(id):
    """Retrieve students information on HTTP body.

    Args:
        id (int, optional): Student ID to retrieve data from DB.
    Returns:
        HTTP Code: Success if data exists, No Content otherwise.
        Body: Student information if ID as used as argument. Complete
        list of students information otherwise.
    Note:
        Not required to insert body in HTTP request.
    """
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
    """Insert student data into database.
    
    Use the body of the HTTP POST request to send student data to DB.
    A typical request would include a student's name, it's system
    identifier and a list of projects already done, if it exists.

    Returns:
        HTTP Code: 'Created' if body is valid, 'Not Authorized' otherwise.
        Body: Request body is succesfull, error code description otherwise.
    """
    student = Student(request, db)
    db.students.insert_one(student())
    student().pop("_id")
    return jsonify(student()), 201

#################
# DELETE Method # 
#################

@application.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    """Remove student data from database

    Args:
        id (int): Student unique identifer on the database to remove
    Returns:
        HTTP Code: 'Success' if id exists and data deleted.
                   'Not Found' if data doesn't exist.
        Body: {} if request was succesful, error message otherwise.
    """
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
