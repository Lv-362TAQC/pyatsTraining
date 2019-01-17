""" HW01 task

Write one test for each function located in calculation.py module. The tests have to be a part of one class.
Also, a user needs to pass num1 and num2 while running the tests. By default, num1 = 3 , num2 = 0 .
If there are math errors (like ZeroDivisionError ), make a test as passx .
If the calculated value is less than 0, please skip the test.
All other cases have to be considered as passed.
"""


def add(num1, num2):
    """Add two numbers"""
    return num1 + num2


def divide(num1, num2):
    """Divide two numbers"""
    return num1 / num2
