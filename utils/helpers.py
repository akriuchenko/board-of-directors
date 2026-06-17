import logging
from datetime import datetime
from config import CREWAI_LOG_LEVEL

# Setup logging
logging.basicConfig(
    level=CREWAI_LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('board_of_directors.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def log_message(message: str, level: str = "INFO"):
    """Log a message at the specified level"""
    if level == "DEBUG":
        logger.debug(message)
    elif level == "INFO":
        logger.info(message)
    elif level == "WARNING":
        logger.warning(message)
    elif level == "ERROR":
        logger.error(message)
    elif level == "CRITICAL":
        logger.critical(message)


def format_output(title: str, content: str) -> str:
    """Format output with title and content"""
    separator = "=" * 80
    return f"""
{separator}
{title.upper()}
{separator}
{content}
{separator}
"""


def print_section(title: str, content: str):
    """Print a formatted section"""
    print(format_output(title, content))


def get_timestamp():
    """Get current timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
