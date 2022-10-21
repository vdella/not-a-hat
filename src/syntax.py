from ply import yacc


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


def p_PARAMLISTCALL(p):
    """
    PARAMLISTCALL :
    """
    pass


def p_PRINTSTAT(p):
    pass


def p_READSTAT(p):
    pass


def p_RETURNSTAT(p):
    pass


def p_IFSTAT(p):
    pass


def p_FORSTAT(p):
    pass


def p_STATELIST(p):
    pass


def p_ALLOCEXPRESSION(p):
    pass


def p_EXPRESSION(p):
    pass


def p_NUMEXPRESSION(p):
    pass


def p_TERM(p):
    pass


def p_UNARYEXPR(p):
    pass


def p_FACTOR(p):
    pass


def p_LVALUE(p):
    pass
