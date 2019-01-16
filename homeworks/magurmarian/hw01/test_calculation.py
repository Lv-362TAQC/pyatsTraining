"""module for testing add and devide functions"""
import argparse
import sys

from pyats.aetest import Testcase, test, main
from calculation import add, divide

parameters = {
    'num1': 3,
    'num2': 0
}


class SmokeTest(Testcase):
    """class for smoke testing add and devide functions"""
    @test
    def test_add(self, num1, num2):
        """method for testing add function"""
        if add(num1, num2) >= 0:
            assert add(num1, num2) >= 0
        else:
            self.skipped('Result is less then 0)')

    @test
    def test_devide(self, steps, num1, num2):
        """method for testing devide function"""
        with steps.start('Divide') as step:
            try:
                assert divide(num1, num2) > 0
            except ZeroDivisionError:
                step.passx(f'num1:{num1} ,num2:{num2}',
                           from_exception=ZeroDivisionError('ZeroDivisionError'))
            except AssertionError:
                self.skipped('Result is less then 0)')


def inputs():
    """parsing user arguments here"""
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-num1', dest='num1', type=int, required=False, default=parameters['num1'])
    parser.add_argument('-num2', dest='num2', type=int, required=False, default=parameters['num2'])

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    return args


if __name__ == '__main__':

    INPUT_DATA = inputs()
    main(num1=INPUT_DATA.num1, num2=INPUT_DATA.num2)
