from pyats.aetest import Testcase, test
from calculation import multiplication


class TryTest(Testcase):

    @test
    def multiplication(self, num1, num2):
        if multiplication(num1, num2) < 0:
            self.failed('Result < 0)')
