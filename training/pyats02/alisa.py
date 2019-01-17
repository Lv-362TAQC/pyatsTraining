from pyats.aetest import Testcase, test, main


class Smoke(Testcase):

    @test
    def test_one(self):
        print('Alisa is fine!')


class Health(Testcase):

    @test
    def status(self):
        print('Alisa\'s health is fine!')


if __name__ == '__main__':
    main()
