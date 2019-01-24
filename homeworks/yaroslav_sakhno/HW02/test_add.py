from pyats.aetest import Testcase, test
from calculation import add


class TryTest(Testcase):

    @test
    def add(self, num1, num2):
        if add(num1, num2) < 0:
            self.failed('Result < 0)')
