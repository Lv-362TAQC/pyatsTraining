"""Homework #2 by Yaroslav Sakhno

Task description:
There are two numbers. Each of them can be negative, floating etc. You need to create a job which will accept two
numbers as the arguments. This job has to run in parallel 4 different tests: multiplication, division, addition,
subtraction. Each of these tests will perform an appropriate math operation on given numbers. A test has to fail if
the calculation result is less then 0, otherwise, the test is passed.
"""

def multiplication(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2
