from flask import jsonify


class HttpError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def response(self):
        response = {'error': self.message}
        return jsonify(response)


class HttpBadRequestError(HttpError):
    def __init__(self, message):
        super().__init__(400, message)


class HttpNotFoundError(HttpError):
    def __init__(self, message):
        super().__init__(404, message)
