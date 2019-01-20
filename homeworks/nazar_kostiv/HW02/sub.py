from pyats.aetest import Testcase, test


class Math(Testcase):

    @test
    def subtraction(self, num1, num2):
        if num1 - num2 < 0:
            self.failed(f'Result "{num1}" - "{num2}" is less than 0')
