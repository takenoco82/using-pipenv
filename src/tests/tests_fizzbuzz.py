import unittest

from nose.plugins.attrib import attr
from parameterized import param, parameterized

from server import app, fizzbuzz


@attr(size='Small')
class TestFizzBuzz(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand(
        [
            param("value_1", input=1, expected="1"),
            param("value_2", input=2, expected="2"),
            param("value_3", input=3, expected="Fizz"),
            param("value_4", input=4, expected="4"),
            param("value_5", input=5, expected="Buzz"),
            param("value_6", input=6, expected="Fizz"),
            param("value_10", input=10, expected="Buzz"),
            param("value_15", input=15, expected="FizzBuzz"),
            param("value_30", input=15, expected="FizzBuzz"),
        ]
    )
    def test_fizzbuzz_logic_normal(self, _, input, expected):
        actual = fizzbuzz.fizzbuzz_logic(input)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            param("value_1", input=1, expected=['1']),
            param("value_1", input=15, expected=[
                '1',
                '2',
                'Fizz',
                '4',
                'Buzz',
                'Fizz',
                '7',
                '8',
                'Fizz',
                'Buzz',
                '11',
                'Fizz',
                '13',
                '14',
                'FizzBuzz'
            ]),
        ]
    )
    def test_fizzbuzz_gen_normal(self, _, input, expected):
        for index, actual in enumerate(fizzbuzz.fizzbuzz_gen(input)):
            self.assertEqual(actual, expected[index])

    @parameterized.expand(
        [
            param(
                "value_minus",
                input=-1,
                expected={
                    "exception": ValueError,
                    "message": "`-1` is invalid value. must be larger than `0`.",
                },
            ),
            param(
                "value_0",
                input=0,
                expected={
                    "exception": ValueError,
                    "message": "`0` is invalid value. must be larger than `0`.",
                },
            ),
            param(
                "type_str",
                input="hoge",
                expected={
                    "exception": TypeError,
                    "message": "`hoge` is invalid value. must be type `int`.",
                },
            ),
            param(
                "type_bool",
                input=True,
                expected={
                    "exception": TypeError,
                    "message": "`True` is invalid value. must be type `int`.",
                },
            ),
            param(
                "type_float",
                input=1.2,
                expected={
                    "exception": TypeError,
                    "message": "`1.2` is invalid value. must be type `int`.",
                },
            ),
        ]
    )
    def test_fizzbuzz_gen_exeption(self, _, input, expected):
        try:
            fizzbuzz.fizzbuzz_gen(input)
        except expected["exception"] as e:
            message = e.args[0]
            self.assertEqual(message, expected["message"])


@attr(size='Medium')
class TestFizzBuzz_Medium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.url = '/v1/fizzbuzz/{n}'

    def tearDown(self):
        pass

    def test_2xx(self):
        url = self.url.format(n=5)
        response = self.app.get(url)

        self.assertEqual(response.status_code, 200)

        response_body = response.get_json()
        self.assertEqual(response_body['fizzbuzz'], ['1', '2', 'Fizz', '4', 'Buzz'])

    def test_4xx(self):
        url = self.url.format(n=0)
        response = self.app.get(url)

        self.assertEqual(response.status_code, 400)

        response_body = response.get_json()
        self.assertEqual(response_body['error'], '`0` is invalid value. must be larger than `0`.')
