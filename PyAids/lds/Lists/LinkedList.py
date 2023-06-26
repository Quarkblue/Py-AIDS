from .Node import Node

class LinkedList:
    """
    Creates a linked list object with a head node.
    """
    
    def __init__(self, head=None):
        """
        ----------
        Parameters
        ----------
        head : any, optional
            The value of the head node. The default is None.
        """
        if head == None:
            self.head = None
        else:
            self.head = Node(head)
    
    def __str__(self):
        if self.head == None:
            return "None"
        elif self.head.next_node == None:
            return f"{self.head.value}"
        else:
            str_str = ""
            current = self.head
            while current.next_node != None:
                str_str += f"{current.value} --> "
                current = current.next_node
            
            str_str += f"{current.value}"
            return str_str
        
    def __repr__(self):
        repr_str = f"LinkedList({self.__str__()})"
        return repr_str
        
    def __len__(self):
        if self.head == None:
            return 0
        else:
            count = 1
            current = self.head
            while current.next_node != None:
                count += 1
                current = current.next_node
            return count
    
    
    def insert_end(self, value):
        """
        Inserts a node at the end of the linked list.
        ----------
        Parameters
        ----------
        value : any
            The value of the node to be inserted.
        """
        if self.head == None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next_node != None:
                current = current.next_node
            current.next_node = Node(value)
    
    def insert_begin(self, value):
        """
        Inserts a value at the beginning of the linked list.
        ----------
        Parameters
        ----------
        value : any
            The value of the node to be inserted.
        """
        if self.head == None:
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
    
    
    def insert(self, value, index):
        """
        Inserts a value at any given index in the linked list.
        ----------
        Parameters
        ----------
        value : any
            The value of the node to be inserted.
        index : int
            The index at which the node is to be inserted.
        """
        if index == 0:
            self.insert_begin(value)
        elif index == len(self):
            self.insert_end(value)
        else:
            current = self.head
            for i in range(index-1):
                current = current.next_node
            current.next_node = Node(value, current.next_node)
            
            
            
    def search(self, value):
        """
        Searches for the given value in the linked list.
        ----------
        Parameters
        ----------
        value : any
            The value to be searched.
        -------
        Returns
        -------
        bool
            True if the value is present in the linked list, else False.
        """
        if self.head == None:
            return False
        else:
            current = self.head
            while current != None:
                if current.value == value:
                    return True
                current = current.next_node
            return False
    
    def index(self, value):
        """
        Returns the index of the given value in the linked list.
        ----------
        Parameters
        ----------
        value : any
            The value whose index is to be returned.
        
        -------
        Returns
        -------
        int
            The index of the given value.
        """
        index = None
        if self.head == None:
            return index
        else:
            index = 0
            if self.head.value == value:
                return index
            else:
                current = self.head
                while current.next_node != None:
                    index += 1
                    if current.next_node.value == value:
                        return index
                    current = current.next_node
    
    def __getitem__(self, index):
        if self.head == None:
            raise IndexError("The linked list is empty.")
        else:
            if index == 0:
                return self.head
            else:
                current = self.head
                for i in range(index):
                    current = current.next_node
                return current
        
            
    def delete_begin(self):
        """
        Deletes the first node of the linked list.
        """
        if self.__len__() == 0:
            raise ValueError("The linked list is empty.")
        else:
            current = self.head
            self.head = self.head.next_node
            del current
    
    def delete_end(self):
        """
        Deletes the last node of the linked list.
        """
        if self.__len__() == 0:
            raise ValueError("The linked list is empty.")
        else:
            current = self.head
            while current.next_node.next_node != None:
                current = current.next_node
            current.next_node = None
            
    def delete_index(self, index: int):
        """
        Deletes a node at any given index in the linked list.
        ----------
        Parameters
        ----------
        index : int
            The index at which the node is to be deleted.
        """
        if self.__len__() == 0 or index > self.__len__() or index < 0:
            raise IndexError("The linked list is empty.")
        else:
            if index == 0:
                self.delete_begin()
            elif index == len(self)-1:
                self.delete_end()
            else:
                current = self.head
                for i in range(index-1):
                    current = current.next_node
                current.next_node = current.next_node.next_node
    
    def delete_value(self, value):
        """
        Deletes the first occurence of the given value in the linked list.
        ----------
        Parameters
        ----------
        value : any
            The value to be deleted.
        """
        if self.__len__() == 0:
            raise ValueError("The linked list is empty.")
        else:
            if self.search(value):
                self.delete_index(self.index(value))

            else:
                raise ValueError("The value is not present in the linked list.")
            
    def update(self, index, value: any, next_n: Node = None):
        """
        Modifies the Node at the given index.
        ----------
        Parameters
        ----------
        index : int
            The index of the node to be modified.
        value : any
            The new value of the node.
        next_n : Node, optional
            The new next node of the node, default in None.
        """
        if self.__len__() == 0:
            raise IndexError("The linked list is empty.")
        else:
            if index == 0 and next_n is None:
                self.head.value = value
                
            elif next_n is None:
                current = self.head
                for i in range(index):
                    current = current.next_node
                current.value = value
                
            elif next_n is not None and type(next_n) == Node:
                current = self.head
                for i in range(index):
                    current = current.next_node
                current.value = value
                current.next_node = next_n
            elif type(next_n) != Node:
                raise TypeError("The parameter next_n must be of type Node.")
        
    
    def reverse(self):
        """
        Reverses the linked list.
        """
        if self.__len__() == 0:
            raise ValueError("The linked list is empty.")
        else:
            current = self.head
            prev = None
            while current != None:
                next_node = current.next_node
                current.next_node = prev
                prev = current
                current = next_node
            self.head = prev
    
    def concatenate(self, other):
        """
        Concatenates the given linked list to the end of the current linked list.
        """
        if self.__len__() == 0:
            self.head = other.head
        elif other.__len__() == 0:
            pass
        else:
            current = self.head
            while current.next_node != None:
                current = current.next_node
                
            current.next_node = other.head
    
    def swap(self, index1, index2):
        """
        Swaps two nodes in the linked list.
        ----------
        Parameters
        ----------
        index1 : int
            The index of the first node to be swapped.
        index2 : int
            The index of the second node to be swapped.
        """
        if self.__len__() == 0:
            raise IndexError("The linked list is empty.")
        elif self.__len__() == 1:
            raise IndexError("The list has only one element.")
        else:
            if index1 == 0:
                current1 = self.head
            else:
                current1 = self.head
                for i in range(index1):
                    current1 = current1.next_node
            
            if index2 == 0:
                current2 = self.head
            else:
                current2 = self.head
                for i in range(index2):
                    current2 = current2.next_node
            
            temp = current1.value
            current1.value = current2.value
            current2.value = temp
    
            
    def sorted(self, ascending: bool = True):
        """
        Checks if the linked list is sorted or not.
        ascending : bool, optional
            Check if the sort is ascending or descending, default is True(ascending).
        """
        if self.__len__() == 0:
            raise ValueError("The linked list is empty.")
        else:
            if ascending == True:
                current = self.head
                while current.next_node != None:
                    if current.value > current.next_node.value:
                        return False
                    current = current.next_node
                return True
            else:
                current = self.head
                while current.next_node != None:
                    if current.value < current.next_node.value:
                        return False
                    current = current.next_node
                return True
    
    def sort(self, ascending=True):
        """
        Sorts the linked list.
        ascending : bool, optional
            True: sort in ascending order
            False: sort in descending order
            default: True
        """
        if self.__len__() == 0:
            return None
        else:
            if self.sorted(ascending=ascending):
                return
            else:
                values = self.to_list()
                values.sort(reverse= not ascending)
                self.create_from_list(values)
        
    
    
    """
    Custom methods for creating and converting linked lists.
    """
    
    
    def to_list(self):
        """
        creates a list of the values of the linked list.
        -------
        Returns
        -------
        list
            A list of the values of the linked list.
        """
        if self.__len__() == 0:
            return []
        else:
            current = self.head
            values = []
            while current != None:
                values.append(current.value)
                current = current.next_node
            return values
    
    

    def create_from_list(self, array: list):
        """
        Create a linked list from a list
        ----------
        Parameters
        ----------
        array : list
            The list to be converted to a linked list.
            
        """
        if len(array) == 0:
            self.head = None
        else:
            self.head = Node(array[0])
            current = self.head
            for i in range(1, len(array)):
                current.next_node = Node(array[i])
                current = current.next_node
    
    def __getDuplicates(self, list):
        """
        Finds the duplicates in a list.
        """
        duplicates = []
        for i in list:
            if list.count(i) > 1:
                duplicates.append(i)
        return duplicates
    
    
    def create_from_dict(self, dictionary: dict):
        """
        Creates a linked list from a dictionary with the keys as the values of the nodes and the values as the next nodes.
        The first key is the value of the head node.
        ----------
        Parameters
        ----------
        dictionary : dict
            The dictionary to be converted to a linked list.
        """
        if len(dictionary) == 0:
            self.head = None
        else:
            keys = list(dictionary.keys())
            if len(keys) > len(set(keys)):
                raise ValueError(f"The keys of the dictionary must be unique. There are duplicates in the keys: {self.__getDuplicates(keys)}")
            
            elif len(keys) == len(set(keys)):
                if None in dictionary.values():
                    raise ValueError("The values of the dictionary must not be None.")
                elif len(dictionary.values()) == 1:
                    self.head = Node(list(dictionary.keys())[0])
                else:
                    self.head = Node(list(dictionary.keys())[0])
                    self.head.next_node = Node(dictionary[self.head.value])
                    current = self.head.next_node
                    values = list(dictionary.values())
                    keys_new = [x for x in keys if x in values]
                    for i in keys:
                        if i not in keys_new:
                            del dictionary[i]
                    print(dictionary)
                    values = list(dictionary.values())
                    for i in range(1, len(keys_new)):
                        current.next_node = Node(dictionary[current.value])
                        current = current.next_node
                    
                    current.next_node = Node(dictionary[current.value])
                    
            