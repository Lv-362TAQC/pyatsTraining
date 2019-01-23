mapping = {
    'a': (1, 3, 4, 5, 6, 7, 8),
    'b': (0, 2, 3, 4),
    'c': (7, 9, 0, 6, 5, 4, 3, 1),
}


class Test(Testcase):
    @setup
    def setup(self, letter):
        pass

    @test
    def check(self, number):
        print(f'number:	{number}')
