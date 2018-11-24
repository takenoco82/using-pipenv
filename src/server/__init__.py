from flask import Flask
from server import fizzbuzz


apis = [
    fizzbuzz.app,
]

app = Flask(__name__)

# Blueprint の登録
for api in apis:
    app.register_blueprint(api, url_prefix="/v1")
