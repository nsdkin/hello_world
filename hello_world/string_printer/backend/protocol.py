# -*- coding: utf-8 -*-

import typing


@typing.runtime_checkable
class StringPrinterBackend(typing.Protocol):
    def print_string(self, string: str) -> None: ...
