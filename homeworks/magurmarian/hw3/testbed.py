from pyats.utils.fileutils import FileUtils
from pyats.aetest import Testcase, test


class Smoke(Testcase):
    @test
    def copy_to_local_pc(self, tb):
        with FileUtils(testbed=tb) as futils:
            futils.copyfile(
                source='scp://192.168.195.143/home/adminaccount/some.txt',
                destination='/home/marian/github/pyatsTraining/homeworks/magurmarian/hw3')

    @test
    def copy_to_remote_pc(self, tb):
        with FileUtils(testbed=tb) as futils:
            futils.copyfile(
                source='/home/marian/github/pyatsTraining/homeworks/magurmarian/hw3/some.txt',
                destination='scp://192.168.195.143/home/adminaccount')
