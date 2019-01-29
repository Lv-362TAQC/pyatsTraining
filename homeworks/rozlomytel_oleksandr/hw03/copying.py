from pyats.aetest import Testcase, test
from pyats.utils.fileutils import FileUtils


class Smoke(Testcase):

    @test
    def copying_to_local(self, env):
        with FileUtils(testbed=env) as futils:
            futils.copyfile(
                source='scp://rrr//home/adminaccount/test.txt',
                destination='/home')

    @test
    def copying_to_vm(self,env):
        with FileUtils(testbed=env) as futils:
            futils.copyfile(
                source='/home/test1.txt',
                destination='scp://rrr//home/adminaccount/')
