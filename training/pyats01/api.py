from pyats.aetest import Testcase, test, main


class SmokeTest(Testcase):

    @test
    def test_passed(self):
        self.passed('passed')

    @test
    def test_failed(self):
        self.failed('failed because of ...')

    @test
    def test_errored(self):
        self.errored('Hmmmm....', from_exception=ValueError('Nothing! But needs something!'))

    @test
    def test_skipped(self):
        self.skipped('Someone other is guilty!')

    @test
    def test_blocked(self):
        self.blocked('I need a pen.....')

    @test
    def test_aborted(self):
        self.aborted('I do not want to work!')

    @test
    def test_passx(self):
        self.passx('passx!!!')


if __name__ == '__main__':
    main()
