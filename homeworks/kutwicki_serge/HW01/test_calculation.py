"""Homework_01 pyATS. Test for calculation.py"""
# pylint: disable=C0103 - ignore constant name "parameters"

import argparse
import sys

from calculation import add, divide
from pyats.aetest import Testcase, test, main

parameters = {
    'num1': 3,
    'num2': 0
}


class SmokeTest(Testcase):
    """Smoke test"""

    @test
    def test_add(self, steps, num1, num2):
        """Test addition functionality."""
        with steps.start(f'Addition of {num1} and {num2}'):
            summ = add(num1, num2)
            if summ < 0:
                self.skipped(f'Test was skipped because result of adding {num1} and {num2} is less then 0')
            else:
                assert summ == num1 + num2

    @test
    def test_divide(self, steps, num1, num2):
        """Test division functionality."""
        with steps.start(f'Division of {num1} by {num2}') as step:
            try:
                div_result = divide(num1, num2)
                if div_result < 0:
                    self.skipped(f'Test was skipped because result of division {num1} by {num2} is less then 0')
                else:
                    assert div_result == num1 / num2
            except ZeroDivisionError:
                step.passx(f'Division of {num1} by {num2}', from_exception=ZeroDivisionError('ZeroDivisionError'))


def inputs():
    """Arguments parser setup."""
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-num1', dest='num1', type=int, required=False, default=parameters['num1'])
    parser.add_argument('-num2', dest='num2', type=int, required=False, default=parameters['num2'])

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    return args


if __name__ == '__main__':
    INPUT_DATA = inputs()
    main(num1=INPUT_DATA.num1, num2=INPUT_DATA.num2)
