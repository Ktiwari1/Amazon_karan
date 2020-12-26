import logging
import inspect

class Baseclass:
    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("C:\\Users\\Karan's PC\\PycharmProjects\\AmazonAutomationframework\\reports\\log.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

