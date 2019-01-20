from pyats.aetest import Testcase, test, main
from calculation import add, divide, multiplication, subtract


class TryTest(Testcase):

    @test
    def add(self,steps, num1, num2):
        with steps.start('Add'):
            assert add(num1,num2) == num1 + num2
        with steps.start('Result > 0'):
            try:
                assert add(num1, num2) > 0
            except AssertionError:
                self.failed('Result < 0)')

    @test
    def divide(self, num1, num2):
        try:
            assert divide(num1, num2) == num1 / num2
        except ZeroDivisionError:
            self.failed('passx')

    @test
    def multiplication(self, steps, num1, num2):
        with steps.start('Add'):
            assert multiplication(num1, num2) == num1 * num2
        with steps.start('Result > 0'):
            try:
                assert multiplication(num1, num2) > 0
            except AssertionError:
                self.failed('Result < 0)')

    @test
    def subtract(self, steps, num1, num2):
        with steps.start('Add'):
            assert subtract(num1, num2) == num1 - num2
        with steps.start('Result > 0'):
            try:
                assert subtract(num1, num2) > 0
            except AssertionError:
                self.failed('Result < 0)')
