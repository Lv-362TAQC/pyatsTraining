import argparse
import sys
from pyats.aetest import Testcase, test, main
from calculation import add, divide

parameters = {
        'num1': 3,
        'num2': 0
    }

class SmokeTest(Testcase):
    parameters = {
        'num1': 3,
        'num2': 0
    }

    @test
    def test_add(self, steps, num1, num2):
        with steps.start('Add') as step:
            assert add(num1, num2) == num1 + num2
        with steps.start('Result bigger then 0') as step:
            try:
                assert add(num1, num2) > 0
            except AssertionError:
                self.skipped('Result is less then 0)')




    @test
    def test_devide(self, steps, num1, num2):
        with steps.start('Divide') as step:
            try:
                result = divide(num1, num2)
                assert result > 0
            except ZeroDivisionError:
                step.passx(f'num1:{num1} ,num2:{num2}', from_exception=ZeroDivisionError('ZeroDivisionError'))
            except AssertionError:
                self.skipped('Result is less then 0)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-num1', dest='num1', type=int, required=False)
    parser.add_argument('-num2', dest='num2', type=int, required=False)

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    main(num1=args.num1, num2=args.num2)
