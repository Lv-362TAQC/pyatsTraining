from pyats.easypy.tasks import run


def main(runtime):
    run(testscript='connections.py', device=runtime.testbed.devices['vm'])
