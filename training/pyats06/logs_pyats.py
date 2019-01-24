from pyats.log import ScreenHandler, TaskLogHandler, ScreenFormatter, TaskLogFormatter

# help(ScreenHandler)
# help(TaskLogHandler)
# help(ScreenFormatter)
# help(TaskLogFormatter)
import sys
import logging

logger = logging.getLogger(__name__)

# handler example
handler = ScreenHandler()
handler = ScreenHandler(sys.stdout)
logger.addHandler(handler)
logger.critical('a critical message')

# task log example
handler = TaskLogHandler('./TaskLog-A.log')
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.info('an info message')
