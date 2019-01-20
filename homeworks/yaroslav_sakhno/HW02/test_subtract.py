from pyats.aetest import Testcase, test
from calculation import subtract


class TryTest(Testcase):

    @test
    def subtract(self, num1, num2):
        if subtract(num1, num2) < 0:
            self.failed('Result < 0)')
