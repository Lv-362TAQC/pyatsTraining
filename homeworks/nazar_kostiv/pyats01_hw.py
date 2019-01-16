"""Homework #1 by Nazar K.

Task:
Write one test for each function located in calculation.py module.
The tests have to be a part of one class.
Also, a user needs to pass num1 and num2 while running the tests.
By default, num1 = 3 , num2 = 0 .
If there are math errors (like ZeroDivisionError ), make a test as passx .
If the calculated value is less than 0 , please skip the test.
All other cases have to be considered as passed."""

# pylint: disable=C0103

import argparse
import sys
from pyats.aetest import Testcase, test, main
from calculation import add, divide


class SmokeTest(Testcase):
    """Smoke tests for calculation.py"""

    @test
    def test_add(self, steps, num1, num2):
        """Test 'add' func in calculation.py.
        Test will be skipped if result less then 0 and passed in other cases"""
        with steps.start('Result bigger or equal 0'):
            if add(num1, num2) < 0:
                self.skipped('Result is less then 0)')

    @test
    def test_divide(self, steps, num1, num2):
        """Test 'divide' func in calculation.py.
        Test will be skipped if result less then 0, passx in case when result is 0
        and passed in other cases."""
        with steps.start('Divide'):
            try:
                assert divide(num1, num2) >= 0
            except ZeroDivisionError:
                self.passx(f'num1:{num1} ,num2:{num2}',
                           from_exception=ZeroDivisionError('ZeroDivisionError'))
            except AssertionError:
                self.skipped('Result is less then 0')


if __name__ == '__main__':
    parameters = {
        'num1': 3,
        'num2': 0
    }
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-num1', dest='num1', type=int, required=False, default=parameters['num1'])
    parser.add_argument('-num2', dest='num2', type=int, required=False, default=parameters['num2'])
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    main(num1=args.num1, num2=args.num2)
