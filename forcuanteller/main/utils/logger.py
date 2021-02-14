import logging
import loguru


class Logger:
    """
    Setting up logger for the project. The log will be logged within the file as well
    logger.setup_logger(script_name) must be called first before using the logger.
    """

    def __init__(self):
        self.logger = loguru.logger
        self.file_index = None
        self.level = logging.DEBUG

    def info(self, msg):
        if logging.INFO >= self.level:
            return self.logger.opt(depth=1).info(msg)

    def debug(self, msg):
        if logging.DEBUG >= self.level:
            return self.logger.opt(depth=1).debug(msg)

    def error(self, msg):
        if logging.ERROR >= self.level:
            return self.logger.opt(depth=1).error(msg)

    def warning(self, msg):
        if logging.WARNING >= self.level:
            return self.logger.opt(depth=1).warning(msg)


logger = Logger()
