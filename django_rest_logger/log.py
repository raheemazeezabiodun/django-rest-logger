import logging
import sys

from django.conf import settings


def exception():
    """
    Log an exception during execution.

    This method should be used whenever an user wants to log a generic exception that is not
    properly managed.

    :param exception:
    :return:
    """
    logger = logging.getLogger(settings.LOGGER_EXCEPTION)
    logger.exception(msg=sys.exc_info()[1])


def error(message, details, status_code):
    """
    Log an error occurred during execution.

    This method should be used when an exception is properly managed but shouldn't occur.

    Args:
        message: message identifying the error
        details: dict with context details
        status_code: http status code associated with the error
    Returns:

    """
    assert isinstance(message, str)
    assert isinstance(details, dict)
    assert isinstance(status_code, int)

    details['http_status_code'] = status_code

    logger = logging.getLogger(settings.LOGGER_ERROR)
    logger.exception(msg=message, extra=details)


def warning(message, details):
    """
    Log a warning message during execution.

    This method is recommended for cases when behaviour isn't the appropriate.

    Args:
        message: message identifying the error
        details: dict with context details

    Returns:

    """
    assert isinstance(message, str)
    assert isinstance(details, dict)

    logger = logging.getLogger(settings.LOGGER_WARNING)
    logger.warning(msg=message, extra=details)
