from pyats.aetest import Testcase, test
from calculation import divide


class TryTest(Testcase):

    @test
    def divide(self, num1, num2):
        try:
            if divide(num1, num2) < 0:
                self.failed('Result < 0)')
        except ZeroDivisionError:
            self.passed('ZeroDivisionError but we decided pass this test')
