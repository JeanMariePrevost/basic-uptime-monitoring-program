import os
from src.backend.logging.bump_logging import general_logger, monitor_logger


def test_loggers_exist():
    # Check if loggers exist
    assert general_logger is not None
    assert monitor_logger is not None


def test_loggers_have_handlers():
    # Check if loggers have handlers
    assert len(general_logger.handlers) > 0
    assert len(monitor_logger.handlers) > 0


def test_logs_directory_created():
    # Check if the logs directory was created
    assert os.path.exists("logs")
