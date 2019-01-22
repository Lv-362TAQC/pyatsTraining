from pyats.topology import loader, Device
from pyats.aetest import Testcase, test, main


class Smoke(Testcase):

    @test
    def defaut_connection(self, device: Device):
        device.connect()  # == self.vm.connectionmgr.connect()
        device.execute('hostname')
        device.disconnect()

    @test
    def test_connection(self, device: Device):
        device.connect(via='test', alias='test')
        device.test.execute('hostname')
        device.test.disconnect()

    @test
    def multiple_connections(self, device: Device):
        device.connect(via='main', alias='main')
        device.main.ping('108.177.119.103')
        device.connect(via='test', alias='test')
        device.test.execute('hostname')
        device.disconnect_all()


if __name__ == '__main__':
    testbed = loader.load('test-env.yaml')
    main(device=testbed.devices['vm'])
