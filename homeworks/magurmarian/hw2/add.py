"""module for testing functions"""
from pyats.aetest import Testcase, test


class Math(Testcase):
    """class for testing add function"""
    @test
    def test_add(self, num1, num2):
        """method for testing add function"""
        if num1 + num2 < 0:
            self.failed('Result of add is less then 0')
