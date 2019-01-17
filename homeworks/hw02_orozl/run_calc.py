import argparse
import sys
from pyats.easypy import Task


def new_task(runtime, test, num1, num2):
    return Task(testscript=test, runtime=runtime, num1=num1, num2=num2)


parser = argparse.ArgumentParser(description="Two numbers for calculating")
parser.add_argument('--num1', required=True, type=int)
parser.add_argument('--num2', required=True, type=int)


def main(runtime):
    test_list = ['calc_addition.py', 'calc_subtraction.py',
                 'calc_division.py', 'calc_multiplication.py']

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    tasks = [new_task(runtime, i, args.num1, args.num2) for i in test_list]

    for task in tasks:
        task.start()
    for task in tasks:
        if task.is_alive():
            task.wait()
