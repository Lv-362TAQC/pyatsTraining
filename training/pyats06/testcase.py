import logging
from pyats.aetest import Testcase, test, main
from moon import a, b, template

_log = logging.getLogger(__name__)


class SmokeTest(Testcase):

    @test
    def test_1(self):
        template(_log, __name__)
        a.a()
        b.b()


if __name__ == '__main__':
    logging.getLogger(__name__).setLevel(logging.DEBUG)
    logging.getLogger('moon').setLevel(logging.CRITICAL)
    logging.getLogger('moon.a').setLevel(logging.DEBUG)
    main()
