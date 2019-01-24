import logging
from pyats.log.utils import banner, title

logger = logging.getLogger(__name__)
# banners
logger.warning(banner('an informational message banner'))
logger.warning(banner('an error message\nwith newline'))
logger.warning(banner('aReallyLongMessageThatIsLongerThanMaxWidthIsChoppedUp', width=40))
# titles
logger.warning(title('an informational message title'))
logger.warning(title('an error message\nwith newline'))
logger.warning(title('a message', margin='!'))
