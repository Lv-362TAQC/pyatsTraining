"""Base math functions for the HW02."""


def add(num1, num2):
    """Add two numbers"""
    return num1 + num2


def subtract(num1, num2):
    """Subtract two numbers"""
    return num1 - num2


def multiply(num1, num2):
    """Multiply two numbers"""
    return num1 * num2


def divide(num1, num2):
    """Divide two numbers"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        return -1
