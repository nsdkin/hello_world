# -*- coding: utf-8 -*-

import sys
from .protocol import StringPrinterBackend


class StdoutStringPrinterBackend(StringPrinterBackend):
    @staticmethod
    def _is_line_terminated(string: str) -> bool:
        return string.endswith('\n')

    def print_string(self, string: str) -> None:
        if not self._is_line_terminated(string):
            string += '\n'

        sys.stdout.write(string)
        return
