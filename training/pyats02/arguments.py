import time
from pyats.aetest import Testcase, test, main


class Smoke(Testcase):

    @test
    def test(self, duration, interval):
        print(f'Duration: {duration}; interval: {interval}')
        if duration > 50:
            self.failed('Too big duration!')
        time.sleep(interval)


if __name__ == '__main__':
    main(duration=23, interval=1)
