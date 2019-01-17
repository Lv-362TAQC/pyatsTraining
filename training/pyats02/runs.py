# runs.py
from pyats.easypy import run


def main(runtime):
    # using run() api to run a task, save the result to variable
    # (max_runtime = 60*5 seconds = 5 minutes)
    for duration in range(0, 100, 20):
        result = run(testscript='arguments.py',
                     runtime=runtime,
                     taskid=f'duration [{duration}] | interval [2]',
                     max_runtime=60 * 5,
                     duration=duration, interval=2)
        # check whether the next script should continue
        # based on previous task's results.
        if not result:
            break
