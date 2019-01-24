import sys
import argparse
from pyats.aetest import Testcase, test, main, loop

mapping = {
    'a': (1, 3, 4, 5, 6, 7, 8),
    'b': (0, 2, 3, 4),
    'c': (7, 9, 0, 6, 5, 4, 3, 1)
}

parser = argparse.ArgumentParser(description="Parsing letter for mapping")
parser.add_argument('--letter', required=True, type=str)
args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])


class Test(Testcase):

    letter = mapping[args.letter]

    @loop(number=mapping[args.letter])
    @test
    def check(self, number):
        print(f'number: {number}')


if __name__ == "__main__":
    main()