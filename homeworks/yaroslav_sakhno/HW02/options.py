from pyats.easypy import Task


def new_task(runtime, num1):
    return Task(testscript='test_calculatin.py', runtime=runtime, num1=num1, num2=2)


def main(runtime):
    tasks = [new_task(runtime, num1) for num1 in range(-5, 5)]
    for task in tasks:
        task.start()
    # wait for completion
    for task in tasks:
        if task.is_alive():
            task.wait()
