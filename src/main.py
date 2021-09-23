#
# main.py
#
# Authors: Artur Barichello
#          Lucas Verdade
#          Lucas Zacchi
#
#

from argparse import Namespace
import sys
import ply.yacc as yacc
from lexer import Lexer
from output import (
    parse_arguments,
    InvalidTokenError,
)
from pprint import pprint

# Ply necessary imports
from lexer import TOKENS as tokens
from syntax import *
from parser import syntax_lexer

# import logging
#
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logger = logging.getLogger()

# Isso limita o traceback para aparecer só o erro criado
# sys.tracebacklimit = 0


def main(args: Namespace) -> None:
    with open(args.src) as f:
        src = f.read()

    lexer = Lexer()
    lexer.build()
    lexer.input(src)

    try:
        token_list = lexer.token_list()
    except InvalidTokenError as err:
        sys.exit(-1)

    # Prints da entrega 1:
    # print_tokens(token_list)
    # print_symbol_table(token_list)
    # print_separator()

    try:
        syntax_parser = yacc.yacc(start="PROGRAM", check_recursion=True)
        syntax_result = syntax_parser.parse(src, debug=args.debug, lexer=syntax_lexer)
    except Exception as error:
        print(f"Erro na etapa de análise sintática: {error}")
        sys.exit(-1)

    print("Análise sintática feita com sucesso! Não houveram erros!")

    try:
        syntax_parser = yacc.yacc(start="PROGRAM", check_recursion=True)
        result = syntax_parser.parse(src, debug=args.debug, lexer=lexer)
    except Exception as error:
        print(f"Erro na etapa de análise semântica: {error}")
        sys.exit(-1)
    print("Análise semântica feita com sucesso! Não houveram erros!")


if __name__ == "__main__":
    args = parse_arguments()
    main(args)
