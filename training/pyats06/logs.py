import logging
from pyats.aetest import Testcase, test, main

_log = logging.getLogger(__name__)


class SmokeTest(Testcase):

    @test
    def test_1(self):
        _log.debug('debug message')
        _log.info('info message')
        _log.warning('warning message')
        _log.critical('critical message')
        _log.error('error message')


if __name__ == '__main__':
    main()
