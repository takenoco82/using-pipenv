from flask import Blueprint
from server.exceptions import HttpNotFoundError

app = Blueprint('NotFound', __name__)


@app.route('/NotFound', methods=['GET'])
def bad_request():
    raise HttpNotFoundError('Not Found')
