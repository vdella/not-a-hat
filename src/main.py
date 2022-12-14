from argparse import Namespace
import sys

from lex import Lexer
from reader import parse_arguments
from writer import print_separator
from token_list import TokenList
from symbol_table import SymbolTable

# Ply necessary imports
from syntax import *
from parser import syntax_lexer

# Isso limita o traceback para aparecer só o erro criado
# sys.tracebacklimit = 0


def main(vargs: Namespace) -> None:
    with open(vargs.src) as f:
        src = f.read()

    lexer = Lexer()
    lexer.build()
    lexer.input(src)

    try:
        tokens = Lexer.tokens
    except Exception as err:
        print(f"Tokenization error: {err}")
        sys.exit(-1)

    # Prints da entrega 1:
    tokens = TokenList(tokens)
    print(tokens)

    symbol_table = SymbolTable()
    print(token_list)
    print_separator()

    try:
        syntax_result = yacc.yacc(
            debug=vargs.debug,
        ).parse(src, debug=vargs.debug, lexer=syntax_lexer)
    except Exception as error:
        print(f"Erro na etapa de análise sintática: {error}")
        sys.exit(-1)

    print("Análise sintática feita com sucesso! Não houveram erros!")

    try:
        syntax_parser = yacc.yacc(start="PROGRAM", check_recursion=True, debug=False)
        result = syntax_parser.parse(src, debug=False, lexer=lexer)
        print_separator()
        print("Syntax parser result:\n")
        pprint(result)
    except Exception as error:
        print(f"Erro na etapa de análise semântica: {error}")
        sys.exit(-1)
    print("Análise semântica feita com sucesso! Não houveram erros!")


if __name__ == "__main__":
    args = parse_arguments()
    main(args)
