from .base_mixins import BaseLoggingMixin
import logging
import os

logger = logging.getLogger(os.getenv('TRACKING_LOGGER'))


class LoggingMixin(BaseLoggingMixin):
    def handle_log(self):
        """
        Hook to define what happens with the log.

        Defaults on saving the data on the db.
        """
        if self.log['status_code'] == 200:
            logger.info(self.log)
        else:
            logger.error(self.log)


class LoggingErrorsMixin(LoggingMixin):
    """
    Log only errors
    """

    def should_log(self, request, response):
        return response.status_code >= 400
