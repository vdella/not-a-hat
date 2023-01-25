from collections import deque
from typing import List, Optional, Union, Dict, Tuple, Any, Deque
from table import EntryTable
from exceptions import VariableInScopeError


class Scope:
    def __init__(self, outer_scope=None, loop=False) -> None:
        self.entry_table: List[EntryTable] = []
        self.outer_scope: Optional[Scope] = outer_scope
        self.inner_scopes: List = []
        self.loop: bool = loop

    def __str__(self) -> str:
        return str(entry for entry in self.entry_table)

    def add_entry(self, entry: EntryTable) -> None:
        has_var, lineno = self.contains_var(entry.label)

        if has_var:
            raise VariableInScopeError(
                f"Variável {entry.label} na linha {entry.lineno} já foi declarada na linha {lineno}"
            )
        self.entry_table.append(entry)

    def add_inner_scope(self, scope: Any) -> None:
        self.inner_scopes.append(scope)

    def contains_var(self, var_label: str) -> Tuple[bool, Union[int, None]]:
        for entry in self.entry_table:
            if entry.label == var_label:
                return True, entry.lineno
        return False, None

    def as_dict(self) -> Dict:
        return {
            "table": [entry.as_dict() for entry in self.entry_table],
            "inner_scopes": [scope.as_dict() for scope in self.inner_scopes],
        }


class ScopeStack:
    def __init__(self) -> None:
        self.stack: Deque[Scope] = deque()

    def __len__(self) -> int:
        return len(self.stack)

    def is_empty(self) -> bool:
        return True if len(self.stack) == 0 else False

    def length(self) -> int:
        return len(self.stack)

    def push(self, x: Scope) -> None:
        self.stack.append(x)

    def pop(self) -> Scope:
        return self.stack.pop()

    def seek(self) -> Optional[Scope]:
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
