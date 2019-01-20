from pyats.aetest import Testcase, test


class Math(Testcase):

    @test
    def division(self, num1, num2):
        try:
            if num1 / num2 < 0:
                self.failed(f'Result "{num1}" / "{num2}" is less than 0')
        except ZeroDivisionError:
            self.passed(f'Test passed, but "ZeroDivisionError" raised')
