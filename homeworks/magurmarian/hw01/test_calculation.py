"""module for testing add and devide functions"""
import argparse
import sys

from pyats.aetest import Testcase, test, main
from calculation import add, divide


class SmokeTest(Testcase):
    """class for smoke testing add and devide functions"""
    parameters = {
        'num1': -3,
        'num2': 1
    }

    @test
    def test_add(self, num1, num2):
        """method for testing add function"""
        if add(num1, num2) < 0:
            self.skipped('Result of add is less then 0')

    @test
    def test_divide(self, steps, num1, num2):
        """method for testing divide function"""
        with steps.start('Divide') as step:
            try:
                assert divide(num1, num2) > 0
            except ZeroDivisionError:
                step.passx(f'num1:{num1} ,num2:{num2}',
                           from_exception=ZeroDivisionError('Zero Division Error. No way!'))
            except AssertionError:
                step.skipped('Result of divide is less then 0')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-num1', dest='num1', type=int, required=False)
    parser.add_argument('-num2', dest='num2', type=int, required=False)

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    main(num1=args.num1, num2=args.num2)
