# -*- coding: utf-8 -*-

import typing
from .backend.protocol import StringPrinterBackend


@typing.runtime_checkable
class StringPrinter(typing.Protocol):
    def get_string(self) -> str: ...
    def set_string(self, string: str) -> None: ...
    def print_string(self) -> None: ...
