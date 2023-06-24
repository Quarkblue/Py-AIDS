from .Node import Node

class DoublyLinkedList:
    """
    Creates a double linked list object
    
    ----------
    Attributes
    ----------
        head: Node
            The head of the linked list
    
    -------
    Methods
    -------
        insert_end(value: any): None
            inserts the value in the end of the list.
        insert_begin(value: any): None
            inserts the value in the beginning of the list.
        insert(value: any, index: int): None
            inserts the value at the given index.
        search(value: any): bool
            returns True if the value is in the list, False otherwise.
        index(value: any): int
            retruns the index of the value if it is in the list, None otherwise.
        delete_begin(): None
            deletes the first item in the list
        delete_end(): None
            deletes the last item in the list
        delete_index(index: int): None
            deletes the item at the given index
        delete_value(value: any): None
            deletes the first occurence of the value in the list
        get_first(): any
            returns the first value in the list
        get_last(): any
            returns the last value in the list
        reverse(): None
            reverses the list
        concatenate(other: DoublyLinkedList): None
            concatenates the other list to the current list at the end
        to_list(): list
            returns a list of the values in the linked list
        from_list(array: list): None
            creates a linked list from the given array
    """
    
    def __init__(self, head=None) -> None:
        """
        ----------
        Parameters
        ----------
            head: any
                The head of the linked list
        """
        if head is None:
            self.head = None
        else:
            self.head = Node(head)
        
        
    def __str__(self) -> str:
        if self.head == None:
            return "None"
        elif self.head.next_node == None:
            return f"None <-- {self.head.value} --> None"
        else:
            current = self.head
            string = "None <-- "
            while current.next_node != None:
                string += f"{current.value} <--> "
                current = current.next_node
            
            string += f"{current.value} --> None"
            
            return string
        
    def __repr__(self) -> str:
        repr_str = f"DoublyLinkedList({self.__str__()})"
        return repr_str
    
    def __len__(self) -> int:
        if self.head == None:
            return 0
        else:
            current = self.head
            count = 1
            while current.next_node != None:
                count += 1
                current = current.next_node
            return count
        
        
    def __getitem__(self, index: int):
        if index >= self.__len__() or index < 0:
            raise IndexError("Index out of range.")
        else:
            current = self.head
            for i in range(index):
                current = current.next_node
            return current.value
        
    def insert_end(self, value):
        """
        Inserts the value in the end of the list.
        ----------
        Parameters
        ----------
            value: any
                The value to be inserted
        """
        if self.head == None:
            self.head = Node(value)
        elif(self.head.next_node == None):
            self.head.next_node = Node(value, prev_node=self.head)
        else:
            current = self.head
            while current.next_node != None:
                current = current.next_node

            current.next_node = Node(value, prev_node=current)
            
            
    
    def insert_begin(self, value):
        """
        inserts the value in the beginning of the list.
        ----------
        Parameters
        ----------
            value: any
                The value to be inserted
        """
        if self.head == None:
            self.head = Node(value)
        else:
            self.head.prev_node = Node(value, next_node=self.head)
            self.head = self.head.prev_node
            
    def insert(self, value: any, index: int):
        """
        inserts the value at the given index.
        ----------
        Parameters
        ----------
            value: any
                The value to be inserted
            index: int
                The index at which the value is to be inserted
        """
        if index == 0:
            self.insert_begin(value)
        elif index == self.__len__():
            self.insert_end(value)
        else:
            if index > self.__len__() or index < 0:
                raise IndexError("Index out of range.")
            else:
                current = self.head
                for i in range(index):
                    current = current.next_node
                
                current = Node(value, prev_node=current.prev_node, next_node=current)
                current.prev_node.next_node = current
                current.next_node.prev_node = current
    
    def search(self, value):
        """
        Returns true if the value is in the list, false otherwise.
        ----------
        Parameters
        ----------
            value: any
                The value to be searched
        """
        if self.head == None:
            return False
        else:
            current = self.head
            while current.next_node != None:
                if current.value == value:
                    return True
            
            return False
        
    def index(self, value):
        """
        Returns the index of the value if it is in the list, None otherwise.
        ----------
        Parameters
        ----------
            value: any
                The value to be searched
        """
        if self.head == None:
            return None
        elif self.head.value == value:
            return 0
        else:
            current = self.head
            for i in range(self.__len__()):
                if current.value == value:
                    return i
                current = current.next_node
            return None
    
    def delete_begin(self):
        """
        Deletes the first item in the list.
        """
        if self.__len__() == 0:
            raise ValueError("Cannot delete from empty list.")
        elif self.__len__() == 1:
            self.head = None
        else:
            self.head = self.head.next_node
            self.head.prev_node = None
    
    def delete_end(self):
        """
        Deletes the last item in the list.
        """
        if self.__len__() == 0:
            raise ValueError("Cannot delete from empty list.")
        elif self.__len__() == 1:
            self.head = None
        else:
            current = self.head
            while current.next_node != None:
                current = current.next_node
            current.prev_node.next_node = None
            del current

        
    def delete_index(self, index: int):
        """
        Deletes the item at the given index.
        ----------
        Parameters
        ----------
            index: int
                The index at which the value is to be deleted
        """
        if self.__len__() == 0:
            raise IndexError("Index out of range.")
        else:
            if index > self.__len__():
                raise IndexError("Index out of range.")
            elif index < 0:
                raise IndexError("Index out of range.")
            elif index == 0:
                self.delete_begin()
            elif index == self.__len__() - 1:
                self.delete_end()
            else:
                current = self.head
                for i in range(index):
                    current = current.next_node
                current.prev_node.next_node = current.next_node
                current.next_node.prev_node = current.prev_node
                del current

    def delete_value(self, value: any):
        """
        Deletes the first occurence of the given value.
        ----------
        Parameters
        ----------
            value: any
                The value to be deleted
        """
        if self.__len__() == 0:
            raise ValueError("Cannot delete from empty list.")
        elif self.__len__() == 1:
            if self.head.value == value:
                self.head = None
            else:
                raise ValueError("Value not in list.")
        else:
            index = self.index(value)
            if index == None:
                raise ValueError("Value not in list.")
            else:
                self.delete_index(index)
                
    def get_first(self):
        """
        Returns the first item in the list
        """
        if self.head == None:
            return None
        else:
            return self.head
    
    def get_last(self):
        """
        Returns the last item in the list
        """
        if self.__len__() == 0:
            return None
        elif self.__len__() == 1:
            return self.head
        else:
            current = self.head
            while current.next_node != None:
                current = current.next_node
            return current
    
    def reverse(self):
        """
        Reverse the list
        """
        if self.__len__() == 0:
            return None
        elif self.__len__() == 1:
            return self.head
        else:
            current = self.head
            while current.next_node != None:
                current = current.next_node
            
            self.head = current
            while current != None:
                temp = current.next_node
                current.next_node = current.prev_node
                current.prev_node = temp
                current = current.next_node
    
    def concatenate(self, other):
        """
        Concatenate the other list at the end of this list
        ----------
        Parameters
        ----------
            other: DoublyLinkedList
                The list to be concatenated
        """
        if self.__len__() == 0:
            self.head = other.head
        else:
            current = self.get_last()
            current.next_node = other.head
            other.head.prev_node = current
                
                
    # custom methods for conversion
    
    # converts the linked list to a python list
    def to_list(self):
        """
        Returns a list of values in the linked list
        """
        re_lst = []
        if self.head == None:
            return re_lst
        else:
            current = self.head
            for i in range(self.__len__()):
                re_lst.append(current.value)
                current = current.next_node
        
            return re_lst
        
    def from_list(self, array: list):
        """
        Creates a doubly linked list from the given array
        ----------
        Parameters
        ----------
            array: list
                The list to be converted to a doubly linked list
        """
        if len(array) == 0:
            self.head = None
        else:
            self.head = Node(array[0])
            current = self.head
            for i in range(1, len(array)):
                current.next_node = Node(array[i], prev_node=current)
                current = current.next_node