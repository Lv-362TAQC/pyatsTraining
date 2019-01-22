from pyats.aetest import Testcase, test, main


class Smoke(Testcase):

    @test
    def test_one(self, testbed):
        print('alias: ', testbed.devices['main'].alias)
        print('size: ', testbed.devices['main'].custom.size)


if __name__ == '__main__':
    main()
