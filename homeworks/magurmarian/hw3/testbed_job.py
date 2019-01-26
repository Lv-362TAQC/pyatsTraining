from pyats.easypy import run
from pyats.topology import loader

def main():
    env = loader.load('my_yaml.yaml')
    run(testscript="testbed.py", tb=env)
