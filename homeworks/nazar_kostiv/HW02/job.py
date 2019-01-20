"""Homework #2 by Nazar K.

Task:
There are two numbers. Each of them can be negative, floating etc.
You need to create a job which will accept two numbers as the arguments.
This job has to run in parallel 4 different tests: multiplication, division, addition, subtraction.
Each of these tests will perform an appropriate math operation on given numbers.
A test has to fail if the calculation result is less then 0, otherwise, the test is passed."""

# pylint: disable=C0103
import argparse
import sys
from pyats.easypy import Task


def new_task(runtime, test, num1, num2):
    return Task(testscript=test, runtime=runtime, num1=num1, num2=num2)


def main(runtime):
    parser = argparse.ArgumentParser(description="Two numbers for calculating")
    parser.add_argument('-num1', required=False, type=float, default=-5)
    parser.add_argument('-num2', required=False, type=float, default=0)

    tasks_path = ['add.py', 'mul.py', 'sub.py', 'div.py']
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    tasks = [new_task(runtime, path, args.num1, args.num2) for path in tasks_path]
    for task in tasks:
        task.start()
    for task in tasks:
        if task.is_alive():
            task.wait()
