# -*- coding: utf-8 -*-

from .protocol import StringPrinter
from .exceptions import StringNotSetException


class StandardStringPrinter(StringPrinter):

    def __init__(self):
        self._string: str | None = None

    def get_string(self) -> str | None:
        if not self._string:
            raise StringNotSetException
        return self._string

    def set_string(self, string: str) -> None:
        self._string = string

    def print_string(self) -> None:
        return print(self._string)
