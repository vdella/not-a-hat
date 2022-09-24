import ply
from ply.lex import TOKEN
from src.io.reader import read
from src.io.writer import write
from src.symbol_table import SymbolTable


ARITHMETIC_OPERATOR = (
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'MOD'
    )


LOGICAL_OPERATOR = (
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_EQUALS_THAN',
    'GREATER_EQUALS_THAN',
    'EQ_COMPARISON',
    'INEQ_COMPARISON',
)


RESERVED = {
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


EQUALS = ('EQUALS',)


COMMA = ('COMMA',)


BRACKETS = ('LBRACKET',
            'RBRACKET',)


PARENTHESIS = (
    'LPAREN',
    'RPAREN',
)


SQUARE_BRACKETS = ('LSQUAREBRACKET',
                   'RSQUAREBRACKET',)


STRING_LITERAL = ('STRING_LITERAL',)


NUMBER = ('INT', 'FLOAT')


tokens = ARITHMETIC_OPERATOR + LOGICAL_OPERATOR + STRING_LITERAL + ID + \
         COMMA + BRACKETS + NUMBER + EQUALS + PARENTHESIS + SQUARE_BRACKETS + tuple(RESERVED.values())


t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'


t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_EQUALS_THAN = r'<='
t_GREATER_EQUALS_THAN = r'>='
t_EQ_COMPARISON = r'=='
r_INEQ_COMPARISON = r'!='


@TOKEN(r'[a-zA-Z_][a-zA-Z_0-9]*')
def t_ID(t):
    t.type = RESERVED.get(t.value, 'ID')  # Checks for reserved words.
    return t


t_EQUALS = r'='

t_COMMA = r', | ;'

t_LBRACKET = r'\{'
t_RBRACKET = r'\}'

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_LSQUAREBRACKET = r'\['
t_RSQUAREBRACKET = r'\]'

t_STRING_LITERAL = r'".*"'


@TOKEN(r'\d+')
def t_INT(t):
    t.value = int(t.value)
    return t


@TOKEN(r'\d+\.\d+')
def t_FLOAT(t):
    t.value = float(t.value)
    return t


@TOKEN(r'\n+')
def t_newline(t):
    t.lexer.lineno += len(t.value)  # Tracks line numbers.


# A string containing ignored characters (spaces and tabs).
t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    exit(-1)


if __name__ == '__main__':
    data = read('test1.c')
    lexer = ply.lex.lex()
    lexer.input(data)

    symbol_table = SymbolTable(lexer)
    print('Printing test1 symbol table!')

    print('Writing test1 symbol table!')
    write(str(symbol_table), 'symbol_table1.txt')
    print('Done!')
    print()

    data = read('test2.c')
    lexer = ply.lex.lex()
    lexer.input(data)

    symbol_table = SymbolTable(lexer)
    print('Printing test2 symbol table!')

    print('Writing test2 symbol table!')
    write(str(symbol_table), 'symbol_table2.txt')
    print('Done!')
    print()
