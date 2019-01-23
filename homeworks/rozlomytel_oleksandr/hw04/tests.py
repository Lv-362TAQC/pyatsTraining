import argparse
import sys
from pyats.aetest import Testcase, setup, test, loop, main

mapping = {
    'a': (1, 3, 4, 5, 6, 7, 8),
    'b': (0, 2, 3, 4),
    'c': (7, 9, 0, 6, 5, 4, 3, 1),
}


class Test(Testcase):

    @setup
    def setup(self, letter):
        loop.mark(self.check, number=letter)

    @test
    def check(self, number):
        print(f'number: {number}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A letter for mapping")
    parser.add_argument('--letter', required=True, type=str)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    main(letter=mapping[args.letter])
