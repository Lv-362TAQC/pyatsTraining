from pyats.aetest import Testcase, test, main


class Smoke(Testcase):

    @test
    def both(self, foo, bar):
        print(f'foo: {foo}; bar: {bar}')

    @test
    def foo(self, foo):
        print(f'foo: {foo}')

    @test
    def bar(self, bar):
        print(f'bar: {bar}')


if __name__ == '__main__':
    main()
