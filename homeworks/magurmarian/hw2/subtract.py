"""module for testing functions"""
from pyats.aetest import Testcase, test


class Math(Testcase):
    """class for testing subtract function"""
    @test
    def test_subtract(self, num1, num2):
        """method for testing subtract function"""
        if num1 - num2 < 0:
            self.failed('Result of subtract is less then 0')
