from utils import logger as logger_util
logger = logger_util.setup_logging("test")
logger.info("Start")

logger.debug("This is a debug statement")
logger.warning("This is a warning statement")
logger.error("This is an error statement")
logger.critical("This is a critical statement")