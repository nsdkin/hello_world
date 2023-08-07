# -*- coding: utf-8 -*-

import sys
from string_printer.standard_string_printer import StandardStringPrinter
from string_printer.backend.stdout import StdoutStringPrinterBackend


def main() -> None:
    string_printer_backend = StdoutStringPrinterBackend()
    string_printer = StandardStringPrinter(string_printer_backend)
    string_printer.set_string('Hello, world!')
    string_printer.print_string()
    return


if __name__ == "__main__":
    main()
