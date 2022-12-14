from argparse import Namespace
import sys
from reader import parse_arguments
from writer import print_separator
from syntax import *
from parser import syntax_lexer

def main(args: Namespace) -> None:
    with open(args.src) as f:
        src = f.read()

    lexer = Lexer()
    lexer.build()
    lexer.input(src)

    try:
        token_list = lexer.token_list()
    except Exception as err:
        print(f"Erro na etapa de tokenização {err}")
        sys.exit(-1)

    # Prints da entrega 1:
    # print_tokens(token_list)
    # print_symbol_table(token_list)
    print_separator()

    try:
        syntax_result = yacc.yacc(
            debug=args.debug,
        ).parse(src, debug=args.debug, lexer=syntax_lexer)
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
