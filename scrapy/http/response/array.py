"""
This module implements the TextResponse class which adds encoding handling and
discovering (through HTTP headers) to base Response class.

See documentation in docs/topics/request-response.rst
"""

from scrapy.http.response import Response

class ArrayResponse(Response):

    def _set_body(self, body):
        self._body = body
