"""HW02 Division test module"""
from pyats.aetest import Testcase, test
from calculation import divide


class Math(Testcase):
    """Division test"""
    @test
    def test_divide(self, num1, num2):
        """Test division functionality."""
        if divide(num1, num2) < 0:
            self.failed(f'Test failed because result of division {num1} by {num2} is less then 0')
