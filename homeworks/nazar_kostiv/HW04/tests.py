import sys
import argparse
from pyats.aetest import Testcase, test, main, loop, setup

mapping = {
    'a': (1, 3, 4, 5, 6, 7, 8),
    'b': (0, 2, 3, 4),
    'c': (7, 9, 0, 6, 5, 4, 3, 1)
}

class Test(Testcase):

    @setup
    def setup(self, letter):
        if letter in mapping:
            loop.mark(self.check, mapping[letter])
        else:
            self.failed(f'no this letter {letter} in a dict')

    @test
    def check(self, section):
        print(f'number: {section}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parsing letter")
    parser.add_argument('--letter', required=True, type=str)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    main(letter=args.letter)
