from pyats.utils.fileutils import FileUtils
from pyats.aetest import Testcase, test


class Smoke(Testcase):

    @test
    def copy_from(self, env):
        with FileUtils(testbed=env) as futils:
            futils.copyfile(
                source='scp://rrr//home/adminaccount/slavik/3.txt',
                destination='/home/jsakhno/github/pyatsTraining/homeworks/yaroslav_sakhno/hw03')

    @test
    def copy_to(self,env):
        with FileUtils(testbed=env) as futils:
            futils.copyfile(
                source='/home/jsakhno/github/pyatsTraining/homeworks/yaroslav_sakhno/hw03/2.txt',
                destination='scp://rrr//home/adminaccount/slavik')
