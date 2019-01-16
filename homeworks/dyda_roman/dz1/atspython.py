import sys
import argparse

import args
from pyats.aetest import Testcase, test, main
from homeworks.dyda_roman.dz1.calculation import add, divide

parameters = {'num1': 3, 'num2': 0}


class AddDivide(Testcase):

    @test
    def test_for_add(self, num1, num2):
        assert num1 + num2 == add(self.parameters['num1'], self.parameters['num2']) is self.passed('passed')


    @test
    def test_for_divide(self, num1, num2):
        try:
            assert num1 / num2 == divide(self.parameters['num1'], self.parameters['num2']) is self.skipped('min1 / min2 < 0')
        except ZeroDivisionError:
            self.passx('passx')


    @test
    def test_add_skipped(self, num1, num2):
        try:
            assert num1 + num2 < 0
        except AssertionError:
            self.skipped('min1 + min2 < 0')


    # @test
    # def test_divide_skipped(self, num1, num2):
    #     assert num1 / num2 < 0 is self.skipped('min1 / min2 < 0')
    #

if __name__ == '__main__':
        parser = argparse.ArgumentParser(description="standalone parser")
        parser.add_argument('-num1', dest='bigger', type=int, required=False)
        parser.add_argument('-num2', dest='smaller', type=int, required=False)
        # do the parsing
        # always use parse_known_args, as aetest needs to parse any
        # remainder arguments that this parser does not understand
        args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
        # and pass all arguments to aetest.main() as kwargs
        # main(num1=args.bigger, num2=args.smaller)
        main()