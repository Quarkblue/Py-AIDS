class Node:
    """
    Create a node for a linked list.
    """
    def __init__(self, value: any, next_node=None, prev_node=None):
        """
        ----------
        Parameters
        ----------
        value : any
            The value to be stored in the node.
        next_node : Node, optional
            The next node in the linked list. The default is None.
        prev_node : Node, optional
            The previous node in the linked list. The default is None.
        """
        self.prev_node = prev_node
        self.value = value
        self.next_node = next_node
        self.frequency = 0
        self.count = 0
        
    def __repr__(self):
        return f"Node({self.value})"
    
    def __str__(self):
        return f"Node({self.value})"
    
    
    def get_next(self):
        """
        return the next node in the linked list.
        -------
        Returns
        -------
        Node
            The next node in the linked list.
        """
        return self.next_node
    
    def set_next(self, node):
        """
        Set the next node in the linked list.
        ----------
        Parameters
        ----------
        node : Node
            The next node in the linked list.
        """
        self.next_node = node
        
    def set_prev(self, node):
        """
        Set the previous node in the linked list.
        ----------
        Parameters
        ----------
        node : Node
            The previous node in the linked list.
        """
        self.prev_node = node
    
    def get_prev(self):
        """
        Return the previous node in the linked list.
        -------
        Returns
        -------
        Node
            The previous node in the linked list.
        """
        return self.prev_node
        
    def get_value(self):
        """
        Returns the value of the node.
        -------
        Returns
        -------
        any
            The value of the node.
        """
        return self.value
    
    def set_value(self, value: any):
        """
        Set the value of the node
        ----------
        Parameters
        ----------
        value : any
            The value to be stored in the node.
        """
        self.value = value