from dataclasses import dataclass


@dataclass
class EntryTable:
    label: str
    datatype: str
    values: list
    lineno: int

    def as_dict(self) -> dict:
        return {
            "label": self.label,
            "datatype": self.datatype,
            "values": self.values,
            "lineno": self.lineno,
        }
