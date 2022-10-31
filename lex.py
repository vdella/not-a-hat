import ply.lex as lex
from ply.lex import TOKEN, LexToken

from src.io.reader import read
from src.io.writer import write
from src.symbol_table import SymbolTable
from src.token_list import TokenList


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
    'def': 'FUNC_DEF',
    'int': 'INT_TYPE',
    'float': 'FLOAT_TYPE',
    'string': 'STRING_TYPE',
    'new': 'NEW',
    'read': 'READ',
    'null': 'NULL',
    'break': 'BREAK',
    'return': 'RETURN',
    'print': 'PRINT',
}

ID = ('ID',)


ATTRIBUTION = ('ATTRIBUTION',)


COMMA = ('COMMA',)


SEMICOLON = ('SEMICOLON',)


BRACKETS = ('LBRACKET',
            'RBRACKET',)


PARENTHESIS = (
    'LPAREN',
    'RPAREN',
)


SQUARE_BRACKETS = ('LSQUAREBRACKET',
                   'RSQUAREBRACKET',)


STRING_LITERAL = ('STRING_LITERAL',)


INT = ('INT',)
FLOAT = ('FLOAT',)


class Lexer(lex.Lexer):
    tokens = ARITHMETIC_OPERATOR + LOGICAL_OPERATOR + STRING_LITERAL + INT + FLOAT + ID + \
             COMMA + SEMICOLON + BRACKETS + ATTRIBUTION + PARENTHESIS + SQUARE_BRACKETS + \
             tuple(RESERVED.values())

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

    t_ATTRIBUTION = r'='

    t_COMMA = r','
    t_SEMICOLON = r';'

    t_LBRACKET = r'\{'
    t_RBRACKET = r'\}'

    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    t_LSQUAREBRACKET = r'\['
    t_RSQUAREBRACKET = r'\]'

    t_STRING_LITERAL = r'".*"'

    def __init__(self):
        self.__lexer = None
        self.__src = None

    @TOKEN(r'[a-zA-Z_][a-zA-Z_0-9]*')
    def t_ID(self, t: LexToken) -> LexToken:
        t.type = RESERVED.get(t.value, 'ID')  # Checks for reserved words.
        return t

    @TOKEN(r'\d+')
    def t_INT(self, t: LexToken):
        t.value = int(t.value)
        return t

    @TOKEN(r'\d+\.\d+')
    def t_FLOAT(self, t: LexToken):
        t.value = float(t.value)
        return t

    @TOKEN(r'\n+')
    def t_newline(self, t: LexToken):
        t.lexer.lineno += len(t.value)  # Tracks line numbers.

    # A string containing ignored characters (spaces and tabs).
    t_ignore = ' \t'

    def t_error(self, t: LexToken):
        def find_column() -> int:
            line_start = self.__src.rfind("\n", 0, t.lexpos) + 1
            return (t.lexpos - line_start) + 1

        raise Exception(
            f"Invalid character. (line: {t.lineno} | column: {find_column()}) '{t.value[0]}'"
        )

    def build(self, **kwargs):
        self.__lexer = lex.lex(module=self, **kwargs)

    def input(self, src: str, **kwargs):
        self.__src = src
        self.__lexer.input(self.__src, **kwargs)
        self.__lexer.lineno = 1

    def token(self):
        return self.__lexer.token()


if __name__ == '__main__':
    data = read('hello_world.c')

    lexer = Lexer()
    lexer.build()
    lexer.input(data)

    symbol_table = SymbolTable(lexer)
    token_list = TokenList(symbol_table.tokens)

    print('Writing test1 token list!')
    write(str(token_list), 'token_list1.txt')

    print('Writing test1 symbol table!')
    write(str(symbol_table), 'symbol_table1.txt')

    print('Done!')
