from argparse import Namespace
import sys
from reader import parse_arguments
from writer import print_separator
from syntax import *


def main(vargs: Namespace) -> None:
    with open(vargs.src) as f:
        src = f.read()

    analyser = Lexer()
    analyser.build()
    analyser.input(src)

    try:
        analyser.token_list()
    except Exception as err:
        print(f"Tokenization error: {err}")
        sys.exit(-1)

    print_separator()

    try:
        yacc.yacc(
            debug=vargs.debug,
        ).parse(src, debug=vargs.debug, lexer=analyser)
    except Exception as error:
        print(f"Syntax analysis failed: {error}")
        sys.exit(-1)

    try:
        syntax_parser = yacc.yacc(start="PROGRAM", check_recursion=True, debug=False)
        result = syntax_parser.parse(src, debug=False, lexer=analyser)
        print_separator()
        print("Syntax parser result:\n")
        pprint(result)
    except Exception as error:
        print(f"Semantic analysis failed: {error}")
        sys.exit(-1)


if __name__ == "__main__":
    args = parse_arguments()
    main(args)
