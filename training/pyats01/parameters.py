from pyats.aetest import Testcase, test, main

parameters = {
    'a': 10,
    'b': 2
}


class SmokeTest(Testcase):
    parameters = {'c': 3}

    @test
    def test_1(self, a, b):
        print('c: ', self.parameters['c'])
        print('all: ', self.parameters)
        print(f'a:{a} b:{b} ')
        assert a > b, '"a" has to be greater then "b"'


class Redefine(Testcase):
    parameters = {'a': 1}

    @test
    def test_1(self, a, b):
        print(self.parameters)
        print(f'a:{a} b:{b} ')
        assert a > b, f'"a"{a} has to be greater then "b"{b}'


if __name__ == '__main__':
    main()
