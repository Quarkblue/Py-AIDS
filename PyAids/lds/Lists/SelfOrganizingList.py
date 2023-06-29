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
        elif OrgType == "freq":
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
    
    def __organize_transpose(self, node) -> None:
        if node is self.list.head:
            return
        else:
            index = self.list.index(node.value)
            self.list.delete_value(node.value)
            self.list.insert(node.value, index -1)
    
    def __organize_count(self) -> None:
        current = self.list.head
        previous = None
        while current and current.next_node:
            if current.count < current.next_node.count:
                if previous:
                    previous.next_node = current.next_node
                    current.next_node = current.next_node.next_node
                    previous.next_node.next_node = current

                    previous = previous.next_node
                else:
                    self.list.head = current.next_node
                    current.next_node = current.next_node.next_node
                    self.list.head.next_node = current
                    previous = self.list.head
                continue

            previous = current
            current = current.next_node
                    


    def __organize_frequency(self) -> None:
        current = self.list.head
        previous = None
        while current and current.next_node:
            if current.frequency < current.next_node.frequency:
                if previous:
                    previous.next_node = current.next_node
                    current.next_node = current.next_node.next_node
                    previous.next_node.next_node = current

                    previous = previous.next_node
                else:
                    self.list.head = current.next_node
                    current.next_node = current.next_node.next_node
                    self.list.head.next_node = current
                    previous = self.list.head
                continue

            previous = current
            current = current.next_node
        
    
    def __organize(self, node: Node) -> None:
        if self.mtf:
            self.__organize_mtf(node)
        elif self.frequency:
            self.__organize_frequency()
        elif self.Count:
            self.__organize_count()
        elif self.Transpose:
            self.__organize_transpose(node)
            
    def __increase_freq(self) -> None:
        current = self.list.head
        while current is not None:
            current.frequency = current.count / self.total_search
            current = current.next_node
            
    def insert(self, value: any, end: bool = False) -> None:
        if end:
            self.list.insert_end(value)
        else:
            self.list.insert_begin(value)

    
    # search function for the self organizing list
    def search(self, value: any) -> any:
        if len(self.list) == 0:
            raise ValueError("The list is empty.")
        elif len(self.list) == 1:
            self.total_search += 1
            if self.list.head.value == value:
                self.list.head.count += 1
                self.__increase_freq()
                self.__organize(self.list.head)
                return (True, self.list.head)
            else:
                return (False, None)
        else:
            self.total_search += 1
            node = self.list.head
            while node is not None:
                if node.value == value:
                    node.count += 1
                    self.__increase_freq()
                    self.__organize(node)
                    return (True, node)
                else:
                    node = node.next_node
                    
            return (False, None)
        

    def change_heuristic(self, heuristic):
        if heuristic == "mtf":
            self.mtf = True
        elif heuristic == "transpose":
            self.Transpose = True
        elif heuristic == "count":
            self.Count = True
        elif heuristic == "freq":
            self.frequency = True
            
    def delete(self, value: any) -> None:
        self.list.delete_value(value)
    