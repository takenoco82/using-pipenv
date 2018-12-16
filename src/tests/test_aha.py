import time
import unittest

from nose.plugins.attrib import attr


@attr(size='small')
class TestAha(unittest.TestCase):
    _multiprocess_can_split_ = True

    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print("FooTest:setUp_:begin")

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print("FooTest:tearDown_:begin")

    # test routine A
    def testA(self):
        print("FooTest:testA")
        time.sleep(2)

    # test routine B
    def testB(self):
        print("FooTest:testB")

    # test routine C
    def testC(self):
        print("FooTest:testC")

    # test routine D
    def testD(self):
        print("FooTest:testD")

    # test routine E
    def testE(self):
        print("FooTest:testE")
        time.sleep(2)

    # test routine F
    def testF(self):
        print("FooTest:testF")

    # test routine G
    def testG(self):
        print("FooTest:testG")

    # test routine H
    def testH(self):
        print("FooTest:testH")

    # test routine I
    def testI(self):
        print("FooTest:testI")

    # test routine J
    def testJ(self):
        print("FooTest:testJ")
        time.sleep(2)
