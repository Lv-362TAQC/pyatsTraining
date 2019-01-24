def template(log, prefix):
    log.debug(prefix + ': debug message')
    log.info(prefix + ': info message')
    log.warning(prefix + ': warning message')
    log.critical(prefix + ': critical message')
    log.error(prefix + ': error message')
