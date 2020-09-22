#!/usr/bin/python3

class InvalidUsage(Exception):
    """HTTP Error Inherited Class

    Invalid Usage lets the raise of errors at HTTP level,
    allowing the attirbution of custom messages and status
    codes at initilization. It also let custom payload.
    """
    status_code = 400

    def __init__(self, message='Bad Request', status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
