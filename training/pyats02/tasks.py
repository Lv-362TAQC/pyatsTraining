# tasks.py
import time
from pyats.easypy import Task


def new_task(runtime, duration):
    return Task(testscript='arguments.py', runtime=runtime, duration=duration, interval=10)


def main(runtime):
    long_task = new_task(runtime, 30)
    tasks = [new_task(runtime, duration) for duration in range(0, 100, 10)]
    long_task.start()
    long_task.join()
    # start tasks in parallel
    for task in tasks:
        task.start()
    # wait for completion
    for task in tasks:
        if task.is_alive():
            task.wait()
