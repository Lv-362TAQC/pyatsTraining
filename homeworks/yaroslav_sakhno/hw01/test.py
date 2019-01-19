import sys
import argparse
from pyats.aetest import Testcase, test, main
from calculation import add, divide


class TryTest(Testcase):

    @test
    def test_add(self,steps, num1, num2):
        with steps.start('Add'):
            assert add(num1,num2) == num1 + num2
        with steps.start('Result > 0'):
            try:
                assert add(num1, num2) > 0
            except AssertionError:
                self.skipped('Result < 0)')

    @test
    def test_divide(self, num1, num2):
        try:
            assert divide(num1, num2) == num1 / num2
        except ZeroDivisionError:
            self.passx('passx')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="possible configuration options")
    parser.add_argument('-num1', dest='first', type=int, required=False, default=3)
    parser.add_argument('-num2', dest='second', type=int, required=False, default=0)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    main(num1=args.first, num2=args.second)
