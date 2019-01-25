"""module for testing functions"""
from pyats.aetest import Testcase, test


class Math(Testcase):
    """class for divide function"""
    @test
    def test_divide(self, num1, num2):
        """method for testing divide function"""
        try:
            if num1 / num2 < 0:
                self.failed('Result of divide is less then 0')
        except ZeroDivisionError:
            self.passed('Zero division error. No way! ')
