"""
# Logging Configuration Module

This module sets up loggers for the application: 
- general_logger: for any general event and error, *excluding* monitor results (e.g. app launches, user actions, errors, etc.)
- monitor_logger: specifically for logging monitor results and monitoring queries events (e.g. monitor start, stop, success, errors, etc.)

Optionally uses the `colorlog` package for colored console output.
Saves general logs to `logs/app_events.log` and monitor logs to `logs/monitor_results.log`.

Levels of logging are: DEBUG, INFO, WARNING, ERROR, CRITICAL

## Example usage:
```
from bump_logging import general_logger, monitor_logger

general_logger.debug("This is a debug message")
general_logger.info("This is an info message")
general_logger.warning("This is a warning message")
general_logger.error("This is an error message")
general_logger.critical("This is a critical message")

monitor_logger.debug(f"Monitor {monitor_id} started")
monitor_logger.error(f"Monitor {monitor_id} failed to execute, error: {error}")
```

Note to future self:
The loggers are the objects who receive the messages.
The loggers then pass the messages to the handlers.
The handlers format the messages using theit assigned formatters.
The handlers then output the formatted messages to the console, file, or other destinations.

"""

import logging
import os
import backend.settings_manager as settings_manager


try:
    from colorlog import ColoredFormatter  # Optional requirement, only needed for colored console output

    colorlog_available = True
except ImportError:
    colorlog_available = False

general_logger = None
monitor_logger = None


def _initialize_loggers():
    """
    Sets up the loggers for the application.

    It creates the necessary log files and attaches appropriate handlers and formatters to the loggers.
    It is called by the module itself, no need to call it from outside.
    """
    if general_logger and monitor_logger:
        general_logger.warning("Loggers already initialized, are you calling _initialize_loggers() multiple times?")
        return general_logger, monitor_logger

    new_general_logger = logging.getLogger("general")  # App-wide events logging, excluding monitor results
    new_monitor_logger = logging.getLogger("monitor_results")  # Monitor results logging only

    new_general_logger.setLevel(logging.INFO)
    new_monitor_logger.setLevel(logging.INFO)

    general_formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s [%(filename)s:%(lineno)d]")
    monitor_formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s [%(filename)s:%(lineno)d]")

    if colorlog_available:
        # Create a colored formatter for console output if colorlog installed, much better than everything being red
        color_formatter = ColoredFormatter(
            "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt=None,
            reset=True,
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
            secondary_log_colors={},
            style="%",
        )
    else:
        # If colorlog not available, use the same general formatter for console output
        color_formatter = general_formatter

    # Create the various handlers (who print the messages to console, or log it to file)
    # This creates a handler that outputs log messages to the standard error stream (the console here)
    console_handler = logging.StreamHandler()

    try:
        logs_directory = settings_manager.get_value("logs_directory")
        os.makedirs(logs_directory, exist_ok=True)
    except OSError as e:
        input(f"Error creating logs directory: {e}. Press Enter to continue without logging.")

    try:
        general_log_path = os.path.join(logs_directory, "general.log")
        file_handler_general = logging.FileHandler(general_log_path, encoding="utf-8")
    except IOError as e:
        input(f"Error creating general logs file: {e}. Press Enter to continue without logging general events.")

    try:
        file_handler_monitor = logging.FileHandler("logs/monitors.log", encoding="utf-8")
    except IOError as e:
        input(f"Error creating general logs file: {e}. Press Enter to continue without logging monitor events.")

    # Attach formatters to handlers
    console_handler.setFormatter(color_formatter)
    file_handler_general.setFormatter(general_formatter)
    file_handler_monitor.setFormatter(monitor_formatter)

    # Attach handlers to loggers
    new_general_logger.handlers.clear()
    new_monitor_logger.handlers.clear()
    new_general_logger.addHandler(console_handler)
    new_general_logger.addHandler(file_handler_general)
    new_monitor_logger.addHandler(console_handler)
    new_monitor_logger.addHandler(file_handler_monitor)

    return new_general_logger, new_monitor_logger


# Initialize the loggers
general_logger, monitor_logger = _initialize_loggers()
