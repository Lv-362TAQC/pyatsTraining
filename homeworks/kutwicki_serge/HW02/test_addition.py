"""HW02 Addition test module"""
from pyats.aetest import Testcase, test
from calculation import add


class Math(Testcase):
    """Addition test"""
    @test
    def test_add(self, num1, num2):
        """"Test addition functionality."""
        if add(num1, num2) < 0:
            self.failed(f'Test failed because result of adding {num1} and {num2} is less then 0')
