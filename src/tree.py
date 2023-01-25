import uuid
from typing import Optional, Union, Dict


class TreeNode:
    def __init__(
        self,
        left: Optional["TreeNode"],
        right: Optional["TreeNode"],
        value: Optional[Union[str, int, float]],
        res_type: str,
    ) -> None:
        self.id = uuid.uuid4()

        self.value = value
        self.left = left
        self.right = right
        self.res_type = res_type

    def as_dict(self) -> Dict:
        left = None if self.left is None else self.left.as_dict()
        right = None if self.right is None else self.right.as_dict()

        return {
            "value": self.value,
            "right": right,
            "left": left,
        }

    def __str_(self) -> str:
        return f"TreeNode id= {self.id} with value {self.value};"