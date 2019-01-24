import logging
from pyats.easypy import run


def main(runtime):
    logging.getLogger('pyats.aetest.testscript.testcase').setLevel(logging.ERROR)
    logging.getLogger('moon').setLevel(logging.CRITICAL)
    logging.getLogger('moon.a').setLevel(logging.DEBUG)
    run(testscript='testcase.py')
