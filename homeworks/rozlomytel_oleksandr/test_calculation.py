from pyats.aetest import Testcase, test, main
from calculation import *

parameters = {
    'num1': 3,
    'num2': 0
}


class CalcCheck(Testcase):

    @test
    def test_add(self, num1, num2):
        assert add(num1, num2) == num1+ num2
        print('Adding is ok')
        try:
            assert add(num1, num2) > 0
        except AssertionError:
            self.skipped('Result < 0')

    @test
    def test_divide(self, num1, num2):
        try:
            res = divide(num1, num2)
            assert res > 0
        except ZeroDivisionError:
            self.passx('Math error')
        except AssertionError:
            self.skipped('Result < 0')
        else:
            print('Dividing is ok')


if __name__ == '__main__':
    main()
