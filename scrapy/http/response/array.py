"""
This module implements the TextResponse class which adds encoding handling and
discovering (through HTTP headers) to base Response class.

See documentation in docs/topics/request-response.rst
"""
import logging

from scrapy.http.response import Response
logger = logging.getLogger(__name__)

class ArrayResponse(Response):

    def _set_body(self, body):
        logger.info('Body length: %s', len(body))
        self._body = body
