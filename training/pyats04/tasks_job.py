from pyats.easypy import Task


def main():
    tasks = (
        Task(taskid='single letter',
             testscript='tasks.py', foo='f', bar='b'),
        Task(taskid='single number',
             testscript='tasks.py', foo='2', bar='5'),
        Task(taskid='long string',
             testscript='tasks.py', foo='dfgdf', bar='mnfgbgfnbghn'),
        Task(taskid='long numbers',
             testscript='tasks.py', foo='555', bar='34'),
        Task(taskid='empty data',
             testscript='tasks.py', foo='', bar=''),
    )

    for task in tasks:
        task.start()
        task.join()
