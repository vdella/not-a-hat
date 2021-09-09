#
# Authors: Artur Barichello
#          Lucas Verdade
#          Lucas Zacchi

# Structures used to check if binary operations
# are made using valid types


from data import TreeNode
from output import InvalidBinaryOperation

# TODO: fazer enum pra param operation
def check_valid_operation(
    left: TreeNode, right: TreeNode, operation: str, lineno: int
) -> str:
    valid_operations = {
        "+": [
            {"left": "int", "right": "int", "result": "int"},
            {"left": "float", "right": "float", "result": "float"},
            {"left": "string", "right": "string", "result": "string"},
            {"left": "float", "right": "int", "result": "float"},
            {"left": "int", "right": "float", "result": "float"},
        ],
        "-": [
            {"left": "int", "right": "int", "result": "int"},
            {"left": "float", "right": "float", "result": "float"},
            {"left": "float", "right": "int", "result": "float"},
            {"left": "int", "right": "int", "result": "float"},
        ],
        "*": [
            {"left": "int", "right": "int", "result": "int"},
            {"left": "float", "right": "float", "result": "float"},
            {"left": "float", "right": "int", "result": "float"},
            {"left": "int", "right": "float", "result": "float"},
        ],
        "/": [
            {"left": "int", "right": "int", "result": "int"},
            {"left": "float", "right": "float", "result": "float"},
            {"left": "float", "right": "int", "result": "float"},
            {"left": "int", "right": "int", "result": "float"},
        ],
        "%": [
            {"left": "int", "right": "int", "result": "int"},
        ],
    }
    op_list = valid_operations.get(operation)
    if op_list is None:
        raise InvalidBinaryOperation(f"invalid operation {operation}")
    result = list(
        filter(
            lambda op: op["left"] == left.res_type == right.res_type,
            op_list,
        )
    )
    if len(result) == 0:
        raise InvalidBinaryOperation(
            f"can't operate {left.res_type} with {right.res_type}"
        )
    return result[0]["result"]
