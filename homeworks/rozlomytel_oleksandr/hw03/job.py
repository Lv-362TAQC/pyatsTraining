from pyats.easypy.tasks import run
from pyats.topology import loader


def main():
    env = loader.load('tb.yaml')
    run(testscript='test_copy.py', env=env)
