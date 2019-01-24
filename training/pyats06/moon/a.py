import logging
from moon import template

_log = logging.getLogger(__name__)


def a():
    template(_log, 'a')
