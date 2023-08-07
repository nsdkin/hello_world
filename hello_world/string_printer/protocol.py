# -*- coding: utf-8 -*-

import typing


@typing.runtime_checkable
class StringPrinter(typing.Protocol):
    def get_string(self) -> str: ...
    def set_string(self, string: str) -> None: ...
    def print_string(self) -> None: ...
