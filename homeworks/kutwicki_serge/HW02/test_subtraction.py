"""HW02 Subtraction test module"""
from pyats.aetest import Testcase, test
from calculation import subtract


class Math(Testcase):
    """Subtraction test"""
    @test
    def test_subtract(self, num1, num2):
        """Test subtraction functionality."""
        if subtract(num1, num2) < 0:
            self.failed(f'Test failed because result of subtracting {num2} from {num1} is less then 0')
