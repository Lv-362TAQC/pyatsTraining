from pyats.aetest import Testcase, test, main


class SmokeTest(Testcase):

    @test
    def test(self, steps):
        with steps.start('the passed step') as step:
            step.passed('passed')
        with steps.start('Allow next steps', continue_=True) as step:
            step.failed('reason is ...')
        with steps.start('Sub-steps') as long_step:
            with long_step.start('the failed sub-step') as step1:
                step1.failed('reason is ...')
            with long_step.start("Won't be executed") as step2:
                step2.passx('reason is ...')


if __name__ == '__main__':
    main()
