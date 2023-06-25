from .LinkedList import LinkedList

class SOList:
    
    def __init__(self, OrgType: str = "mtf") -> None:
        self.mtf = False
        self.Transpose = False
        self.Count = False
        self.frequency = False
        self.list = LinkedList()
        if OrgType == "mtf":
            self.mtf = True
        elif OrgType == "transpose":
            self.Transpose = True
        elif OrgType == "count":
            self.Count = True
        elif OrgType == "frequency":
            self.frequency = True

    def __str__(self) -> str:
        return str(self.list)
    
    def __repr__(self) -> str:
        return f"SOList({str(self.list)})"

    def __len__(self) -> int:
        return len(self.list)
    
    def insert(self, value: any, end: bool = False) -> None:
        if end:
            pass
        else:
            self.list.insert_begin(value)
            if self.mtf:
                pass
            elif self.Transpose:
                pass
            elif self.Count:
                pass
            elif self.frequency:
                pass
