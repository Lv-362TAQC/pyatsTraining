from pyats.aetest import (
    Testcase, CommonSetup, CommonCleanup,
    subsection, setup, test, cleanup, loop,
    main
)


class Setup(CommonSetup):

    @loop(uids=['up_one', 'up_two'])
    @subsection
    def up(self):
        pass


@loop(uids=['t1', 't2'])
class Test(Testcase):

    @setup
    def test_up(self):
        pass

    @loop(uids=['check1', 'check2'])
    @test
    def check(self):
        pass

    @cleanup
    def test_cleanup(self):
        pass


class Cleanup(CommonCleanup):

    @loop(uids=['clean_one', 'clean_two'])
    @subsection
    def cleanup(self):
        pass


if __name__ == '__main__':
    main()
