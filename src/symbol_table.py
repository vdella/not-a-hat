from tabulate import tabulate


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
        headers = ["Identifier", "Position", "Declaration line", "Reference line"]
        return tabulate([(k,) + v for k, v in self.content.items()], headers=headers, tablefmt='fancy_grid')

    @staticmethod
    def token_list_for(given_lexer) -> list:
        result: list = []

        while True:
            token = given_lexer.token()
            if not token:
                break
            result.append(token)

        return result
