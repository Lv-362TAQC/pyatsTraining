"""HW02 Multiplication test module"""
from pyats.aetest import Testcase, test
from calculation import multiply


class Math(Testcase):
    """Multiplication test"""
    @test
    def test_multiply(self, num1, num2):
        """Test multiplication functionality."""
        if multiply(num1, num2) < 0:
            self.failed(f'Test failed because result of multiplication {num1} and {num2} is less then 0')
