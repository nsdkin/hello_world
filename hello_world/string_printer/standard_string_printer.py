# -*- coding: utf-8 -*-

from .backend.protocol import StringPrinterBackend
from .protocol import StringPrinter
from .exceptions import StringNotSetException


class StandardStringPrinter(StringPrinter):

    def __init__(self, backend: StringPrinterBackend):
        self._string: str | None = None
        self._backend = backend

    def get_string(self) -> str | None:
        if not self._string:
            raise StringNotSetException
        return self._string

    def set_string(self, string: str) -> None:
        self._string = string

    def print_string(self) -> None:
        return self._backend.print_string(self._string)
