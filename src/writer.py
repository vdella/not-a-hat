from pprint import pprint
from tabulate import tabulate

def print_tokens(tokens) -> None:
    result = [(t.type, t.value) for t in tokens]
    pprint("\nPrinting token list: ('Token enumerator', 'Token value'):")
    pprint(result, indent=4)


def print_symbol_table(tokens) -> None:
    print("\nPrinting symbol table:")

    symbol_table: dict = {}
    token_table = [[t.lexpos, t.lineno, t.type, t.value] for t in tokens]

    for token in token_table:
        if token[2] == "LABEL":
            if token[3] in symbol_table:
                symbol_table[token[3]][2].append(token[1])
            else:
                symbol_table[token[3]] = (token[0], token[1], [])

    headers = ["Label", "Index", "Declaration (line)", "Referenced (lines)"]
    print(tabulate([(k,) + v for k, v in symbol_table.items()], headers=headers))
    print_separator()


def print_separator() -> None:
    print("\n===========================\n")
