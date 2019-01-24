import argparse
import sys
from pyats.easypy import Task


def new_task(test, runtime, num1, num2):
    return Task(testscript=test, runtime=runtime, num1=num1, num2=num2)


def main(runtime):
    parser = argparse.ArgumentParser(description="Two numbers for calculating")
    parser.add_argument('-num1', required=False, type=float, default=-3)
    parser.add_argument('-num2', required=False, type=float, default=0)

    tests = ['test_subtract.py', 'test_multiplication.py', 'test_divide.py', 'test_add.py']
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    tasks = [new_task(test, runtime, args.num1, args.num2) for test in tests]
    for task in tasks:
        task.start()
    # wait for completion
    for task in tasks:
        if task.is_alive():
            task.wait()
