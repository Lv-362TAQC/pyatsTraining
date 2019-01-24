from pyats.utils.fileutils import FileUtils
from pyats.topology import loader
TB = loader.load('my_yaml.yaml')


# This with statement ensures that any sessions are automatically closed
# if something goes wrong.
with FileUtils(testbed=TB) as futils:

    # Copy local file to remote location
    futils.copyfile(
        source='scp://192.168.195.143/home/adminaccount/some.txt',
        destination='/home/marian')

    # Copy remote file to local location
    futils.copyfile(
        source='/home/marian/some.txt',
        destination='scp://192.168.195.143/home/adminaccount')

    # Check the existence of a remote file:
    futils.checkfile(
        target='sftp://192.168.195.143/home/adminaccount/some.txt')
