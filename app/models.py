#!/usr/bin/python3

from error import InvalidUsage

class Student():
    """Student DB model to POST requests

    This class defines and process a student
    instance to be inserted onto the database
    via POST HTTP method. It requires db connection
    and the request body and args.
    """

    def __init__(self, request, db):

        fields = ["name", "intra_id", "projects"]

        if not request.json or request.content_type != 'application/json':
            raise InvalidUsage()
        # Don't accept requests without "name" or "intra_id"
        if not all([i in request.json.keys() for i in ["name", "intra_id"]]):
            raise InvalidUsage()
        # Don't accept requests with not defined fields
        if any([i for i in request.json.keys() if i not in fields]):
            raise InvalidUsage()
        if self.__intraid_exists(request.json["intra_id"], db):
            raise InvalidUsage('Not Authorized', 401)

        self.json = request.json
        if "projects" not in self.json:
            self.json["projects"] = []
        if not all([isinstance(i, str) for i in self.json["projects"]]):
            raise InvalidUsage()
        self.json["id"] = self.__auto_increment("id", db.counter)
        pass

    def __call__(self):
        return self.json

    @staticmethod
    def __intraid_exists(intra_id, db):
        query = db.students.find_one({"intra_id": intra_id})
        if query:
            return True
        return False

    @staticmethod
    def __auto_increment(field, collection):
        doc = collection.find_one_and_update(
            {'_id' : field},
            {'$inc': {'sequence_value': 1}})
        return int(doc['sequence_value']);
