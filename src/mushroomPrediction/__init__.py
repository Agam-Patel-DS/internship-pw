import os
import logging
from datetime import datetime
from pathlib import Path

# Create a logs directory if it doesn't exist
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Log file name with timestamp
LOG_FILE = LOGS_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.log"

# Configure logger
logger = logging.getLogger("mushroomPredictionLogger")
logger.setLevel(logging.INFO)

# Formatter
log_formatter = logging.Formatter(
    fmt='[%(asctime)s] [%(levelname)s] %(filename)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# File handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(log_formatter)

# Stream handler (console)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)

# Add handlers (if not already added to avoid duplicates)
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

# Optional: silence overly verbose loggers (e.g., from libraries)
logging.getLogger("urllib3").setLevel(logging.WARNING)
