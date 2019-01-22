from pyats.aetest import Testcase, test, main


class Test(Testcase):

    @test.loop(a=range(10))
    def check(self, a):
        pass


if __name__ == '__main__':
    main()
