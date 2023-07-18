from .Node import Node


class BST:
    
    def __init__(self, root : any = None) -> None:
        if root == None:
            self.root = None
        else:
            self.root = Node(root)
            
    def __str__(self) -> str:
        """
        Return a string representation of the tree.
        """
        return self.__str_repr(self.root, "")
    
    
    def __str_repr(self, node, indent):
        if node is None:
            return ""
        return f"{indent}{node.value}\n" + self.__str_repr(node.left, indent + "left ") + self.__str_repr(node.right, indent + "right ")
    
    def insert(self, value: any) -> None:
        if self.root == None:
            self.root = Node(value)
        else:
            self.__insert_helper(self.root, value)
            
    def __insert_helper(self, node: Node, value: any):
        if node is None:
            node = Node(value)
        elif value > node.value:
            self.__insert_helper(node.right, value)
        elif value <= node.value:
            self.__insert_helper(node.left, value)
    
    def search(self, value: any):
        current = self.root
        
        if current is not None:
            if current.value == value:
                return current
            
            elif current.left is not None and current.value > value:
                current = current.left
                return self.__search_helper(current, value, left = True)
        
            elif current.right is not None and current.value < value:
                current = current.right
                return self.__search_helper(current, value, left = False)
            
    
    
    # testing for this feature is remaining
    def __search_helper(self, node: Node, value: any, left: bool):
        if left:
            if node is None:
                return None
            elif node.value == value:
                return node
            else:
                return self.__search_helper(node.left, value, left=True)
        else:
            if node is None:
                return None
            elif node.value == value:
                return node
            else:
                return self.__search_helper(node.left, value, left=False)
    
    