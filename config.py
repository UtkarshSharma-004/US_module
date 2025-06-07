import logging
import os
from datetime import datetime

def get_Current_time()->str:
    """Get the Current time as a string."""
    return datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def setup_logging():
    """Setup logging configuration to write logs to a file."""
    log_directory = 'logs'
    time = get_Current_time()
    log_file = os.path.join(log_directory, f'{time}.log')

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s- %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    return logging.getLogger(__name__)

if __name__ == '__main__':
    setup_logging()

    logger = logging.getLogger(__name__)

    logger.info("Hello, Universe!")

    logger.warning("This Message is here to warn you ! Check your Collections")
    