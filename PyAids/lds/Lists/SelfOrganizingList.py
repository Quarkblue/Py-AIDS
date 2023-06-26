from .LinkedList import LinkedList
from .Node import Node

class SOList:
    
    def __init__(self, OrgType: str = "mtf") -> None:
        self.mtf = False
        self.Transpose = False
        self.Count = False
        self.frequency = False
        self.total_search = 0
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
    
    
    def __organize_mtf(self, node) -> None:
        if node is self.list.head:
            return
        else:
            self.list.delete_value(node.value)
            self.list.insert_begin(node.value)
    
    def __organize_transpose(self) -> None:
        pass
    
    def __organize_count(self) -> None:
        pass

    def __organize_frequency(self) -> None:
        pass
    
    def __organize(self, node: Node) -> None:
        if self.mtf:
            self.__organize_mtf(node)
        elif self.frequency:
            self.__organize_frequency()
        elif self.Count:
            self.__organize_count()
        elif self.Transpose:
            self.__organize_transpose()
            
            
            
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

    
    # search function for the self organizing list
    def search(self, value: any) -> any:
        if len(self.list) == 0:
            raise ValueError("The list is empty.")
        elif len(self.list) == 1:
            self.total_search += 1
            if self.list.head.value == value:
                self.list.head.count += 1
                self.list.head.frequency = self.list.head.count / self.total_search
                self.__organize(self.list.head)
                return (True, self.list.head)
            else:
                return (False, None)
        else:
            self.total_search += 1
            node = self.list.head
            while node is not None:
                if node.value == value:
                    print(node)
                    node.count += 1
                    node.frequency = node.count / self.total_search
                    self.__organize(node)
                    return (True, node)
                else:
                    node = node.next_node
                    
            return (False, None)
        
