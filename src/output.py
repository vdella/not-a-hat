#
# output.py
#
# Authors: Artur Barichello
#          Lucas Verdade
#          Lucas Zacchi
#
#

from ply.lex import LexToken
from typing import List
from pprint import pprint
from tabulate import tabulate

from itertools import groupby
from operator import itemgetter


class InvalidTokenError(Exception):
    pass


def print_tokens(tokens: List) -> None:
    result = [(t.type, t.value) for t in tokens]
    print("\nPrinting token list: ('Token enumerator', 'Token value'):")
    pprint(result, indent=4)


# TODO: fix symbol table as requested in T1
def print_symbol_table(tokens: List) -> None:
    print("\nPrinting symbol table:")
    table = [[t.lexpos, t.lineno, t.type, t.value] for t in tokens]
    sorted_table = sorted(table, key=lambda x: x[2])
    grouped_table = [
        ([x[1] for x in group], key)
        for key, group in groupby(sorted_table, key=lambda x: x[2])
    ]
    print(tabulate(grouped_table, headers=["Index", "Line", "Type", "Value"]))


def print_separator() -> None:
    print("===========================")
