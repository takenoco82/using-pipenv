from flask import Blueprint
from server.exceptions import HttpBadRequestError

app = Blueprint('BadRequest', __name__)


@app.route('/BadRequest', methods=['GET'])
def bad_request():
    raise HttpBadRequestError('Bad Request')
