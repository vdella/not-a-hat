from ply import yacc
from src.lex import Lexer
from src.io.reader import read


def p_PROGRAM(p) -> None:
    """
    PROGRAM : STATEMENT
            | FUNCLIST
            | empty
    """
    pass


def p_FUNCLIST(p) -> None:
    """
    FUNCLIST : FUNCDEF FUNCLISTTMP
    """
    pass


def p_FUNCLISTTMP(p) -> None:
    """
    FUNCLISTTMP : FUNCLIST
                | empty
    """
    pass


def p_FUNCDEF(p) -> None:
    """
    FUNCDEF : FUNC_DEF ID LPAREN PARAMLIST RPAREN LBRACKET STATELIST RBRACKET
    """
    pass


def p_DATATYPE(p) -> None:
    """
    DATATYPE : INT
             | FLOAT
             | STRING_LITERAL
    """
    pass


def p_PARAMLIST(p) -> None:
    """
    PARAMLIST : DATATYPE ID PARAMLISTTMP
              | empty
    """
    pass


def p_PARAMLISTTMP(p) -> None:
    """
    PARAMLISTTMP : COMMA PARAMLIST
                 | empty
    """
    pass


def p_STATEMENT(p) -> None:
    """
    STATEMENT : VARDECL COMMA
              | ATRIBSTAT COMMA
              | PRINTSTAT COMMA
              | READSTAT COMMA
              | RETURNSTAT COMMA
              | IFSTAT
              | FORSTAT
              | STATELIST_STATEMENT
              | BREAK
              | COMMA
    """
    pass


def p_OPTIONAL_VECTOR(p):
    """
    OPTIONAL_VECTOR : LSQUAREBRACKET INT RSQUAREBRACKET OPTIONAL_VECTOR
                    | empty
    """
    pass


def p_VARDECL(p):
    """
    VARDECL : DATATYPE ID OPTIONAL_VECTOR
    """
    pass


def p_EXPRESSION_CHOOSER(p):
    """
    EXPRESSION_CHOOSER : EXPRESSION
                       | ALLOCEXPRESSION
                       | FUNCCALL
    """
    pass


def p_ATRIBSTAT(p):
    """
    ATRIBSTAT : LVALUE EQUALS LPAREN EXPRESSION_CHOOSER RPAREN
    """


def p_FUNCCALL(p):
    """
    FUNCCALL : ID LPAREN PARAMLIST CALL RPAREN
    """
    pass


def p_INNERPARAMLISTCALL(p):
    """
    INNERPARAMLISTCALL : ID COMMA PARAMLISTCALL
                       | ID
    """
    pass


def p_PARAMLISTCALL(p):
    """
    PARAMLISTCALL : LPAREN INNERPARAMLISTCALL RPAREN
                  | empty
    """
    pass


def p_PRINTSTAT(p):
    """
    PRINTSTAT : PRINT EXPRESSION
    """
    pass


def p_READSTAT(p):
    """
    READSTAT : READ LVALUE
    """
    pass


def p_RETURNSTAT(p):
    """
    RETURNSTAT : RETURN
    """
    pass


def p_IFSTAT(p):
    """
    IFSTAT : IF LPAREN EXPRESSION RPAREN STATEMENT OPTIONAL_ELSE
    """
    pass


def p_OPTIONAL_ELSE(p):
    """
    OPTIONAL_ELSE : LPAREN ELSE STATEMENT RPAREN
                  | empty
    """
    pass


def p_PREPARE_FOR(p):
    """
    PREPARE_FOR : ATRIBSTAT COMMA EXPRESSION COMMA ATRIBSTAT
    """
    pass


def p_FORSTAT(p):
    """
    FORSTAT : FOR LPAREN PREPARE_FOR RPAREN STATEMENT
    """
    pass


def p_INNERSTATELIST(p):
    """
    INNERSTATELIST : STATELIST
                   | empty
    """
    pass


def p_STATELIST(p):
    """
    STATELIST : STATEMENT INNERSTATELIST
    """
    pass


def p_MULTIPLE_NUMEXPRESSIONS(p):
    """
    MULTIPLE_NUMEXPRESSIONS : LSQUAREBRACKET NUMEXPRESSION RSQUAREBRACKET
    """
    pass


def p_OPTIONAL_ALLOC_NUMEXPRESSION(p) -> None:
    """
    OPTIONAL_ALLOC_NUMEXPRESSION : LEFT_SQUARE_BRACKET NUMEXPRESSION RIGHT_SQUARE_BRACKET OPTIONAL_ALLOC_NUMEXPRESSION
                                 | empty
    """
    pass


def p_ALLOCEXPRESSION(p):
    """
    ALLOCEXPRESSION : NEW DATATYPE LEFT_SQUARE_BRACKET NUMEXPRESSION RIGHT_SQUARE_BRACKET OPTIONAL_ALLOC_NUMEXPRESSION
    """
    pass


def p_REL_OP(p):
    """
    REL_OP : LESS_THAN
           | GREATER_THAN
           | LESS_EQUALS_THAN
           | GREATER_EQUALS_THAN
           | EQ_COMPARISON
           | INEQ_COMPARISON
    """
    pass


def p_OPTIONAL_REL_OP_NUMEXPRESSION(p):
    """
    OPTIONAL_REL_OP_NUMEXPRESSION : REL_OP NUMEXPRESSION
                                  | empty
    """


def p_EXPRESSION(p):
    """
    EXPRESSION : NUMEXPRESSION OPTIONAL_REL_OP_NUMEXPRESSION
    """
    pass


def p_NUMEXPRESSION(p):
    """
    NUMEXPRESSION : TERM RECURSIVE_MINUS_OR_PLUS
    """
    pass


def p_RECURSIVE_MINUS_OR_PLUS(p):
    """
    RECURSIVE_MINUS_OR_PLUS : MINUS_OR_PLUS TERM RECURSIVE_MINUS_OR_PLUS
                            | empty
    """
    pass


def p_MINUS_OR_PLUS(p):
    """
    MINUS_OR_PLUS : MINUS
                  | PLUS
    """
    pass


def p_TERM(p):
    """
    TERM : UNARYEXPR RECURSIVE_UNARYEXPR
    """
    pass


def p_RECURSIVE_UNARYEXPR(p):
    """
    RECURSIVE_UNARYEXPR : UNARYEXPR_OPERATOR TERM
                        | empty
    """
    pass


def p_UNARYEXPR_OPERATOR(p):
    """
    UNARYEXPR_OPERATOR : TIMES
                       | DIVISION
                       | MODULO
    """
    pass


def p_UNARYEXPR(p):
    """
    UNARYEXPR : MINUS_OR_PLUS FACTOR | FACTOR
    """
    pass


def p_FACTOR(p):
    """
    FLOAT : INT | FLOAT | STRING_LITERAL | NULL | LVALUE | LPAREN NUMEXPRESSION RPAREN
    """
    pass


def p_LVALUE(p):
    """
    LVALUE : LABEL OPTIONAL_ALLOC_NUMEXPRESSION
    """
    pass


# TODO rewrite grammar and productions within parenthesis.


if __name__ == '__main__':
    data = read('test1.c')

    lexer = Lexer()
    lexer.build()
    lexer.input(data)

    try:
        syntax_result = yacc.yacc().parse(data, lexer=lexer)
    except Exception as error:
        print(f"Erro na etapa de análise sintática: {error}")

    print("Análise sintática feita com sucesso! Não houveram erros!")