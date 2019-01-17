"""Homework_01 pyATS. Test for calculation.py"""
# pylint: disable=C0103 - ignore constant name "parameters"

from pyats.aetest import Testcase, test, main
import argparse
import sys
from calculation import add, divide


class SmokeTest(Testcase):
    """Smoke test"""

    @test
    def test_add(self, steps, num1, num2):
        """Test addition functionality."""
        with steps.start(f'Addition of {num1} and {num2}'):
            if add(num1, num2) < 0:
                self.skipped(f'Test was skipped because result of adding {num1} and {num2} is less then 0')

    @test
    def test_divide(self, steps, num1, num2):
        """Test division functionality."""
        with steps.start(f'Division of {num1} by {num2}'):
            try:
                if divide(num1, num2) < 0:
                    self.skipped(f'Test was skipped because result of division {num1} by {num2} is less then 0')
            except ZeroDivisionError:
                self.passx(f'Division of {num1} by {num2}', from_exception=ZeroDivisionError('ZeroDivisionError'))


def inputs():
    """Arguments parser setup."""
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-num1', dest='num1', type=int, required=False, default=3)
    parser.add_argument('-num2', dest='num2', type=int, required=False, default=0)

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    return args


if __name__ == '__main__':
    input_data = inputs()
    main(num1=input_data.num1, num2=input_data.num2)
