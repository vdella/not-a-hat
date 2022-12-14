from scope import Scope, ScopeStack
from exceptions import VariableNotDeclared
from pprint import pprint


scopes = ScopeStack()


def create_scope(loop: bool):
    """
    Scope management list
    """
    top = scopes.seek()
    new = Scope(outer_scope=top, loop=loop)
    if top:
        top.add_inner_scope(new)
    scopes.push(new)


def variable_type(label: str, lineno: int):  # Used during TreeNode construction in LVALUEs.
    scope = scopes.seek()
    while True:
        for entry in scope.entry_table:
            if entry.label == label:
                return entry.datatype

        scope = scope.outer_scope
        if scope is None:
            break
    raise VariableNotDeclared(f"Undeclared variable '{label}' at line {lineno})")


def numexpressions_from(expressions) -> list:
    exp_dict = list()

    for exp, lineno in expressions:
        if exp.left is None and exp.right is None:
            continue

        exp_dict.append(
            {"Node Id:": str(exp.id), "lineno": lineno, "tree": exp.as_dict()}
        )
    pprint(exp_dict)

    return exp_dict  # As a list of dicts.
