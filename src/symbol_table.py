from prettytable import PrettyTable


class SymbolTable:

    def __init__(self, lexer):
        self.tokens = self.token_list_for(lexer)

        self.content: dict = {}
        digested_tokens = [[t.lexpos, t.lineno, t.type, t.value] for t in self.tokens]

        for token in digested_tokens:
            if token[2] == 'ID':
                if token[3] in self.content:
                    self.content[token[3]][2].append(token[1])
                else:
                    self.content[token[3]] = (token[0], token[1], [])

    def __str__(self):
        printer = PrettyTable()
        printer.field_names = ["Identifier", "Position", "Declaration line", "Reference line"]

        for line in self.content.items():
            identifier = line[0]
            position, declaration_line, reference_line = line[1]

            printer.add_row([identifier, position, declaration_line, reference_line])

        return str(printer)

    @staticmethod
    def token_list_for(given_lexer) -> list:
        result: list = []

        while True:
            token = given_lexer.token()
            if not token:
                break
            result.append(token)

        return result
