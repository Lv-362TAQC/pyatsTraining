from pyats.aetest import Testcase, test, main


class Calc(Testcase):

    @test
    def subtraction(self, num1, num2):
        if num1 - num2 < 0:
            self.failed('Result is less than 0')
        self.passed(f'Result of : {num1} - {num2} is : {num1 - num2}')
