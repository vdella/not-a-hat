from ply import yacc

from lex import Lexer
from reader import read


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
    DATATYPE : INT_TYPE
             | FLOAT_TYPE
             | STRING_TYPE
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
    STATEMENT : VARDECL SEMICOLON
              | ATRIBSTAT SEMICOLON
              | PRINTSTAT SEMICOLON
              | READSTAT SEMICOLON
              | RETURNSTAT SEMICOLON
              | IFSTAT
              | FORSTAT
              | STATELIST_STATEMENT
              | BREAK SEMICOLON
              | SEMICOLON
    """
    pass


def p_STATELIST_STATEMENT(p) -> None:
    """
    STATELIST_STATEMENT : LBRACKET STATELIST RBRACKET
    """
    pass


def p_VARDECL(p) -> None:
    """
    VARDECL : DATATYPE ID OPTIONAL_VECTOR
            | DATATYPE ID ATTRIBUTION ATRIB_RIGHT
    """
    pass


def p_OPTIONAL_VECTOR(p) -> None:
    """
    OPTIONAL_VECTOR : LSQUAREBRACKET INT RSQUAREBRACKET OPTIONAL_VECTOR
                    | empty
    """
    pass


def p_ATRIB_RIGHT(p) -> None:
    """
    ATRIB_RIGHT : ALLOCEXPRESSION
                | EXPRESSION_OR_FUNCCALL
    """
    pass


def p_EXPRESSION_OR_FUNCCALL(p) -> None:
    """
    EXPRESSION_OR_FUNCCALL : PLUS FACTOR RECURSIVE_UNARYEXPR RECURSIVE_MINUS_OR_PLUS OPTIONAL_REL_OP_NUMEXPRESSION
                           | MINUS FACTOR RECURSIVE_UNARYEXPR RECURSIVE_MINUS_OR_PLUS OPTIONAL_REL_OP_NUMEXPRESSION
                           | INT RECURSIVE_UNARYEXPR RECURSIVE_MINUS_OR_PLUS OPTIONAL_REL_OP_NUMEXPRESSION
                           | FLOAT RECURSIVE_UNARYEXPR RECURSIVE_MINUS_OR_PLUS OPTIONAL_REL_OP_NUMEXPRESSION
                           | STRING_LITERAL RECURSIVE_UNARYEXPR RECURSIVE_MINUS_OR_PLUS OPTIONAL_REL_OP_NUMEXPRESSION
                           | NULL RECURSIVE_UNARYEXPR RECURSIVE_MINUS_OR_PLUS OPTIONAL_REL_OP_NUMEXPRESSION
                           | LPAREN NUMEXPRESSION RPAREN RECURSIVE_UNARYEXPR RECURSIVE_MINUS_OR_PLUS OPTIONAL_REL_OP_NUMEXPRESSION
                           | ID FOLLOW_LABEL
    """
    pass


def p_FOLLOW_LABEL(p) -> None:
    """
    FOLLOW_LABEL : OPTIONAL_ALLOC_NUMEXPRESSION RECURSIVE_UNARYEXPR RECURSIVE_MINUS_OR_PLUS OPTIONAL_REL_OP_NUMEXPRESSION
                 | LPAREN PARAMLISTCALL RPAREN
    """
    pass


def p_ATRIBSTAT(p) -> None:
    """
    ATRIBSTAT : LVALUE ATTRIBUTION ATRIB_RIGHT
    """
    pass


def p_PARAMLISTCALL(p) -> None:
    """
    PARAMLISTCALL : ID PARAMLISTCALLTMP
                  | empty
    """
    pass


def p_PARAMLISTCALLTMP(p) -> None:
    """
    PARAMLISTCALLTMP : COMMA PARAMLISTCALL
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
               | RETURN INT
               | RETURN FLOAT
               | RETURN STRING_LITERAL
               | RETURN EXPRESSION_OR_FUNCCALL
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


def p_FORSTAT(p) -> None:
    """
    FORSTAT : FOR LPAREN ATRIBSTAT SEMICOLON EXPRESSION SEMICOLON ATRIBSTAT RPAREN STATEMENT
    """
    pass


def p_STATELIST(p: yacc.YaccProduction) -> None:
    """
    STATELIST : STATEMENT OPTIONAL_STATELIST
    """
    pass


def p_OPTIONAL_STATELIST(p) -> None:
    """
    OPTIONAL_STATELIST : STATELIST
                       | empty
    """
    pass


def p_ALLOCEXPRESSION(p) -> None:
    """
    ALLOCEXPRESSION : NEW DATATYPE LSQUAREBRACKET NUMEXPRESSION RSQUAREBRACKET OPTIONAL_ALLOC_NUMEXPRESSION
    """
    pass


def p_OPTIONAL_ALLOC_NUMEXPRESSION(p) -> None:
    """
    OPTIONAL_ALLOC_NUMEXPRESSION : LSQUAREBRACKET NUMEXPRESSION RSQUAREBRACKET OPTIONAL_ALLOC_NUMEXPRESSION
                                 | empty
    """
    pass


def p_EXPRESSION(p) -> None:
    """
    EXPRESSION : NUMEXPRESSION OPTIONAL_REL_OP_NUMEXPRESSION
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


def p_OPTIONAL_REL_OP_NUMEXPRESSION(p) -> None:
    """
    OPTIONAL_REL_OP_NUMEXPRESSION : REL_OP NUMEXPRESSION
                                  | empty
    """
    pass


def p_NUMEXPRESSION(p) -> None:
    """
    NUMEXPRESSION : TERM RECURSIVE_MINUS_OR_PLUS
    """
    pass


def p_RECURSIVE_MINUS_OR_PLUS(p) -> None:
    """
    RECURSIVE_MINUS_OR_PLUS : MINUS_OR_PLUS TERM RECURSIVE_MINUS_OR_PLUS
                            | empty
    """
    pass


def p_MINUS_OR_PLUS(p) -> None:
    """
    MINUS_OR_PLUS : MINUS
                  | PLUS
    """
    pass


def p_TERM(p) -> None:
    """
    TERM : UNARYEXPR RECURSIVE_UNARYEXPR
    """
    pass


def p_RECURSIVE_UNARYEXPR(p) -> None:
    """
    RECURSIVE_UNARYEXPR : UNARYEXPR_OPERATOR TERM
                        | empty
    """
    pass


def p_UNARYEXPR_OPERATOR(p) -> None:
    """
    UNARYEXPR_OPERATOR : TIMES
                       | DIVIDE
                       | MOD
    """
    pass


def p_UNARYEXPR(p) -> None:
    """
    UNARYEXPR : MINUS_OR_PLUS FACTOR
              | FACTOR
    """
    pass


def p_FACTOR(p):
    """
    FACTOR : INT
           | FLOAT
           | STRING_LITERAL
           | NULL
           | LVALUE
           | LPAREN NUMEXPRESSION RPAREN
    """
    pass


def p_LVALUE(p) -> None:
    """
    LVALUE : ID OPTIONAL_ALLOC_NUMEXPRESSION
    """
    pass


def p_error(p: yacc.YaccProduction) -> None:
    raise Exception(f"Syntax error at token {p}")


def p_empty(p) -> None:
    """
    empty :
    """
    pass


if __name__ == '__main__':
    data = read('hello_world.c')

    lexer = Lexer()
    lexer.build()
    lexer.input(data)

    tokens = lexer.tokens

    _ = yacc.yacc().parse(data, lexer=lexer)
