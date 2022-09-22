import ply.lex
from ply.lex import TOKEN
from src.io.reader import read


ARITHMETIC_OPERATOR = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD'
)


t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'


LOGICAL_OPERATOR = (
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_EQUALS_THAN',
    'GREATER_EQUALS_THAN',
    'EQ_COMPARISON',
    'INEQ_COMPARISON',
)


t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_EQUALS_THAN = r'<='
t_GREATER_EQUALS_THAN = r'>='
t_EQ_COMPARISON = r'=='
r_INEQ_COMPARISON = r'!='


reserved = {
   'if': 'IF',
   'else': 'ELSE',
   'for': 'FOR',
   'while': 'WHILE',
   'def': 'FUNC_DEF',
   'ident': 'IDENT',
   'new': 'NEW_OBJ',
   'constant': 'CONST',
   'null': 'NULL_OBJ',
   'int': 'TYPE_INT',
   'float': 'TYPE_FLOAT',
   'string': 'TYPE_STRING',
   'break': 'BREAK',
   'return': 'RETURN',
   'print': 'PRINT',
}


ID = ('ID',)


@TOKEN(r'[a-zA-Z_][a-zA-Z_0-9]*')
def t_ID(t):
    t.type = reserved.get(t.value, 'ID')  # Checks for reserved words
    return t


EQUALS = ('EQUALS',)


t_EQUALS = r'='


COMMA = ('COMMA',)


t_COMMA = r', | ;'


BRACKETS = ('LBRACKET',
            'RBRACKET',)


t_LBRACKET = r'\{'
t_RBRACKET = r'\}'


PARENTHESIS = (
    'LPAREN',
    'RPAREN',
)


t_LPAREN = r'\('
t_RPAREN = r'\)'


STRING_LITERAL = ('STRING_LITERAL',)


t_STRING_LITERAL = r'".*"'


NUMBER = ('INT', 'FLOAT')


@TOKEN(r'\d+')
def t_INT(t):
    t.value = int(t.value)
    return t


@TOKEN(r'\d+\.\d+')
def t_FLOAT(t):
    t.value = float(t.value)
    return t


# Define a rule so we can track line numbers
@TOKEN(r'\n+')
def t_newline(t):
    t.lexer.lineno += len(t.value)


# Build the lexer
tokens = ARITHMETIC_OPERATOR + LOGICAL_OPERATOR + STRING_LITERAL + ID + \
         COMMA + BRACKETS + NUMBER + EQUALS + PARENTHESIS + tuple(reserved.values())


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    exit(-1)


if __name__ == '__main__':
    # Test it out
    data = read('test1.c')

    lexer = ply.lex.lex()
    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)
