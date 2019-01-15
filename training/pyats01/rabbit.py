from pyats.aetest import (
    Testcase, CommonSetup, CommonCleanup,
    subsection, setup, test, cleanup,
    main
)


class InstallRabbit(CommonSetup):

    @subsection()
    def step_1(self):

        print('Download a Rabbit')


    @subsection
    def step_2(self):
        print('Rabbit is installed')


class SmokeTest(Testcase):

    @setup
    def setup(self):

        print("A setup of smoke test")


    @test
    def test_1(self):
        print('Test #1')


    @test
    def test_2(self):
        print('Test #2')


    @cleanup
    def cleanup(self):
        print("A cleanup of smoke test")


class ConfigurationCheck(Testcase):

    @test
    def something(self):

        print('Rabbit is fine!')


class SmoothClean(CommonCleanup):

    @subsection
    def cleanup(self):

        print('Do nothing')


if __name__ == '__main__':
    main()
