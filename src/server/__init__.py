from flask import Flask
from server import fizzbuzz, error400, error404
from server.exceptions import HttpBadRequestError, HttpNotFoundError


apis = [
    fizzbuzz.app,
    error400.app,
    error404.app,
]

app = Flask(__name__)

# Blueprint の登録
for api in apis:
    app.register_blueprint(api, url_prefix="/v1")


# エラーハンドラーの登録
@app.errorhandler(HttpBadRequestError)
@app.errorhandler(HttpNotFoundError)
def my_error_handler(error):
    return error.response(), error.code
