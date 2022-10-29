from tabulate import tabulate


class TokenList:

    def __init__(self, tokens: list):
        self.__tokens = self.__digest(tokens)

    def __str__(self):
        headers = ["Token enumerator", "Token value"]
        return tabulate([(k, v) for k, v in self.__tokens], headers=headers, tablefmt='fancy_grid')

    @staticmethod
    def __digest(tokens):
        return [(t.type, t.value) for t in tokens]
