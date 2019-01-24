import sys
import argparse
from pyats.aetest import Testcase, test, main, loop, setup

mapping = {
    'a': (1, 3, 4, 5, 6, 7, 8),
    'b': (0, 2, 3, 4),
    'c': (7, 9, 0, 6, 5, 4, 3, 1)
}
parameters = {
    'letter': 'b'
}


class Test(Testcase):

    def get_args():
        print(mapping[parameters['letter']])
        return mapping[parameters['letter']]

    @loop(number=get_args)
    @test
    def check(self, number=1):
        print(f'number: {number}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parsing letter for mapping")
    parser.add_argument('--letter', required=True, type=str, default='a')
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    main(letter=args.letter)
