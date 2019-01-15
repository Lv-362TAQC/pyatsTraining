import sys
import argparse
from pyats.aetest import Testcase, test, main

parameters = {'a': 1}

class SmokeTest(Testcase):

    @test
    def test_1(self, a, b):
        print(self.parameters)
        assert a > b, '"a" has to be greater then "b"'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-a', dest='bigger', type=int, required=False)
    parser.add_argument('-b', dest='smaller', type=int, required=True)
    # do the parsing
    # always use parse_known_args, as aetest needs to parse any
    # remainder arguments that this parser does not understand
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    # and pass all arguments to aetest.main() as kwargs
    data = {
        'b': args.smaller
    }
    if args.bigger:
        data['a'] = args.bigger
    # main(a=args.bigger, b=args.smaller)
    main(**data)
