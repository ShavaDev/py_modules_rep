from logging.config import dictConfig
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOGS_DIR = BASE_DIR / 'logs'
LOGS_DIR.mkdir(parents=True, exist_ok=True)
LOGS_FILE_APP = LOGS_DIR / 'app.log'
LOGS_FILE_ERRORS = LOGS_DIR / 'errors.log'

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s | %(levelname)s | %(name)s | %(module)s:%(lineno)d | %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'WARNING',
            'formatter': 'simple',
            'stream': 'ext://sys.stderr',
        },
        'rotating_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'detailed',
            'filename': LOGS_FILE_APP,
            'maxBytes': 50000,
            'backupCount': 5,
            'encoding': 'utf-8',
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'simple',
            'filename': LOGS_FILE_ERRORS,
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        'app': {
            'level': 'DEBUG',
            'handlers': ['console', 'rotating_file', 'error_file'],
            'propagate': False
        },
        'app.operations': {
            'level': 'DEBUG',
            'handlers': ['rotating_file', 'error_file'],
            'propagate': False
        }
    },
    'root': {
        'level': 'WARNING',
        'handlers': ['console']
    }

}


def setup_logging() -> None:
    dictConfig(LOGGING_CONFIG)
