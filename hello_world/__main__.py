# -*- coding: utf-8 -*-

import sys
from string_printer.standard_string_printer import StandardStringPrinter


def main() -> None:
    string_printer = StandardStringPrinter()
    string_printer.set_string('Hello, world!')
    string_printer.print_string()
    return


if __name__ == "__main__":
    main()
