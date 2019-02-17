from flask import Blueprint, jsonify
from server.exceptions import HttpBadRequestError


app = Blueprint('fizzbuzz', __name__)


@app.route('/fizzbuzz/<int:n>', methods=['GET'])
def fizzbuzz(n: int):
    try:
        response = {'fizzbuzz': list(fizzbuzz_gen(n))}
    except (TypeError, ValueError) as e:
        raise HttpBadRequestError(e.args[0])

    return jsonify(response), 200


def fizzbuzz_gen(n: int):
    if type(n) != int:
        message = "`{}` is invalid value. must be type `int`.".format(n)
        raise TypeError(message)
    if n < 1:
        message = "`{}` is invalid value. must be larger than `0`.".format(n)
        raise ValueError(message)

    for i in range(1, n + 1):
        yield fizzbuzz_logic(i)


def fizzbuzz_logic(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
