"""module for testing functions"""
from pyats.aetest import Testcase, test


class Math(Testcase):
    """class for testing multiplication function"""
    @test
    def test_multiplication(self, num1, num2):
        """method for testing multiplication function"""
        if num1 * num2 < 0:
            self.failed('Result of multiplication is less then 0')
