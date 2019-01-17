# options.py
import sys
import argparse
from pyats.easypy import run

# according to pyATS documentation, define arguments here
parser = argparse.ArgumentParser(description="Possible configuration options")
parser.add_argument('--duration', required=True, type=int, help='How long ...')
parser.add_argument('--interval', required=True, type=int, help='How often ...')


def main():
    # according to pyATS documentation, parse arguments in the `main` method
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    print(args)
    run(testscript='arguments.py', duration=args.duration, interval=args.interval)
