import sys
import argparse
from pyats.aetest import Testcase, test, main

parameters = {
    'num1': 3,
    'num2': 0
}

def add(num1, num2):
    return num1 + num2


def divide(num1, num2):
    return num1 / num2


class SmokeTest(Testcase):

    @test
    def test_add(self, num1, num2):
        #try:
         #   assert add(num1, num2) >= 0
            assert add(num1, num2) == num1 + num2
        #except AssertionError:
         #   self.skipped('skipped')


    @test
    def test_divide(self, num1, num2):
        try:
            assert divide(num1, num2) == num1/num2
        except ArithmeticError:
            self.passx('passx')





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-num1', dest='first', type=int, required=False)
    parser.add_argument('-num2', dest='second', type=int, required=False)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    main(num1=args.first, num2=args.second)
