import sys
import argparse
from pyats.aetest import Testcase, test, main, loop, setup

MAPPING = {
    'a': (1, 3, 4, 5, 6, 7, 8),
    'b': (0, 2, 3, 4),
    'c': (7, 9, 0, 6, 5, 4, 3, 1)
}


class Test(Testcase):

    @setup
    def setup(self, letter):
        try:
            loop.mark(self.check, MAPPING[letter])
        except:
            self.failed("Oops, letter doesn't exist")

    @test
    def check(self, section):
        print(section)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="Parsing letter for mapping")
    PARSER.add_argument('--letter', required=True, type=str)
    ARGS, sys.argv[1:] = PARSER.parse_known_args(sys.argv[1:])

    main(letter=ARGS.letter)
