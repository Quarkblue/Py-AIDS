from .Node import Node


class BST:
    """
    Create a Binary search tree object
    Attributes
    -----------
    root : any
        The root node of the tree
    inorderView : list
    
    Methods
    -------
    insert(value: any)
        Insert a node with given into the tree
    search(value: any)
        Search for a node with given value in the tree
    delete(value: any)
        Delete a node with given value from the tree
    inorder() : List
        Return a list of the inorder traversal of the tree
    preorder()
        Return a list of the preorder traversal of the tree
    postorder()
        Return a list of the postorder traversal of the tree
    height()
        Return the height of the tree
    size()
        Return the size of the tree
    max()
        Return the maximum value in the tree
    min()
        Return the minimum value in the tree
    validate()
        Return True if the tree is a valid BST, False otherwise
    balance()
        Balance the tree
    """
    def __init__(self, root : any = None) -> None:
        """
        Parameters
        ----------
        root: any
            The root node of the tree
        """
        if root == None:
            self.root = None
        else:
            self.root = Node(root)
            
        self.__inorderView = []
        self.__preorderView = []
        self.__postorderView = []
            
    def __str__(self) -> str:
        """
        Return a string representation of the tree.
        """
        return self.__str_repr(self.root, "")
    
    
    def __str_repr(self, node, indent) -> str:
        if node is None:
            return ""
        return f"{indent}{node.value}\n" + self.__str_repr(node.left, indent + "left ") + self.__str_repr(node.right, indent + "right ")
    
    def insert(self, value: any) -> None:
        """
        Insert a node with the given value and balance the tree
        Parameters
        ----------
        value : any
            value for the node to insert
        """
        if self.root == None:
            self.root = Node(value)
        else:
            self.__insert_helper(self.root, value)
        
            self.balance(self.root)
            
            
    def __insert_helper(self, node: Node, value: any) -> None:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.__insert_helper(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.__insert_helper(node.right, value)
        else:
            raise ValueError("Value already exists")
        
    
    def search(self, value: any) -> Node:
        """
        Search the tree for the given value
        Parameters
        ----------
        value : any
            value to search for
        """
        current = self.root
        
        if current is not None:
            if current.value == value:
                return current
            
            elif current.left is not None and value < current.value:
                current = current.left
                return self.__search_helper(current, value, left = True)
        
            elif current.right is not None and value > current.value:
                current = current.right
                return self.__search_helper(current, value, left = False)
            
    def __search_helper(self, node: Node, value: any, left: bool) -> Node:
        if left:
            if node is None:
                return None
            elif node.value == value:
                return node
            elif value > node.value:
                return self.__search_helper(node.right, value, left=False)
            else:
                return self.__search_helper(node.left, value, left=True)
        else:
            if node is None:
                return None
            elif node.value == value:
                return node
            elif value < node.value:
                return self.__search_helper(node.left, value, left=True)
            else:
                return self.__search_helper(node.right, value, left=False)
            
    
            
    def delete(self, value: any) -> None:
        """
        Delete a node with value as the given value
        Parameters
        ----------
        value : any
            value to search for and delete from the tree
        """
        current = self.root
        if current is not None:
            if current.value == value:
                self.root = None
                return current
            
            if value < current.value and current.left is not None:
                if current.left.value == value:
                    current.left = None
                    return current.left
                else:
                    current = current.left
                    return self.__delete_helper(current, value, left=True)
            elif value > current.value and current.right is not None:
                if current.right.value == value:
                    current.right = None
                    return current.right
                else:
                    current = current.right
                    return self.__delete_helper(current, value, left=False)
                
    def __delete_helper(self, node: Node, value: any, left: bool) -> None:
        if left:
            if node is None:
                return None
            elif node.left.value == value:
                temp = node.left.left
                node.left = None
                node.left = temp
                return node.left
            elif node.left is not None:
                if value > node.left.value:
                    return self.__delete_helper(node.left, value, left=False)
            else:
                return self.__delete_helper(node, value, left=True)
        else:
            if node.right is None:
                return None
            elif node.right.value == value:
                temp = node.right.right
                node.right = None
                node.right = temp
                return node.right
            elif node.right is not None: 
                if value < node.right.value:
                    return self.__delete_helper(node, value, left=True)
            else:
                return self.__delete_helper(node, value, left=False)
            
            
    def inorder(self) -> list:
        """
        returns a list of the value of the tree in 'Inorder' sequence
        Returns
        -------
        list
        """
        return self.__inorder_helper(self.root)
    
    
    def __inorder_helper(self, root: Node) -> list:
        if root:
            self.__inorder_helper(root.left)
            self.__inorderView.append(root.value)
            self.__inorder_helper(root.right)
            
        return self.__inorderView
    
    def preorder(self) -> list:
        """
        returns a list of the value of the tree in 'Preorder' sequence
        """
        return self.__preorder_helper(self.root)
    
    def __preorder_helper(self, root: Node) -> list:
        if root:
            self.__preorderView.append(root.value)
            self.__preorder_helper(root.left)
            self.__preorder_helper(root.right)
            
        return self.__preorderView
    
    def postorder(self) -> list:
        """
        returns a list of the value of the tree in 'Postorder' sequence
        """
        return self.__postorder_helper(self.root)
    
    
    def __postorder_helper(self, root: Node) -> list:
        if root:
            self.__postorder_helper(root.left)
            self.__postorder_helper(root.right)
            self.__postorderView.append(root.value)
            
        return self.__postorderView
    
    def height(self) -> int:
        """
        Returns the height of the tree
        Returns
        -------
        int :
            Height of the tree
        """
        return self.__height_helper(self.root)
    
    def __height_helper(self, root: Node) -> int:
        if root is None:
            return 0
        else:
            return max(self.__height_helper(root.left), self.__height_helper(root.right)) + 1
        
        
    def size(self) -> int:
        """
        Returns the size of the tree
        Returns
        -------
        int:
            Size of the tree    
        """
        return self.__size_helper(self.root)
    
    def __size_helper(self, root: Node):
        if root is None:
            return 0
        else:
            return self.__size_helper(root.left) + 1 + self.__size_helper(root.right)
        
        
    def max(self) -> Node:
        """
        Returns the node with the maximum value in the tree
        Returns
        -------
        Node:
            Node object with the maximum value
        """
        return self.__max_helper(self.root)
    
    def __max_helper(self, root: Node) -> Node:
        if root is None:
            return float("-inf")
        else:
            return max(root.value, self.__max_helper(root.left), self.__max_helper(root.right))
        
        
    def min(self) -> Node:
        """
        Returns the node the with least value of all
        Returns
        -------
        Node:
            Node object with the least value
        """
        return self.__min_helper(self.root)
    
    def __min_helper(self, root) -> any:
        if root is None:
            return float("+inf")
        else:
            return min(root.value, self.__min_helper(root.left), self.__min_helper(root.right))        

    def validate(self) -> bool:
        """
        Verifies if the Tree is a valid Binary search tree
        Returns
        -------
        bool :
            True : if the tree is a valid Binary search tree
            False : if the tree is not a valid Binary search tree
        """
        return self.__validate_helper(self.root)
    
    def __validate_helper(self, root: Node) -> bool:
        if root is None:
            return True
        else:
            if root.left is not None and root.left.value > root.value:
                return False
            if root.right is not None and root.right.value < root.value:
                return False
            
            return self.__validate_helper(root.left) and self.__validate_helper(root.right)
    
    def __balance_factor(self, root: Node) -> int:
        if root is None:
            return 0
        else:
            return self.__height_helper(root.left) - self.__height_helper(root.right)
        
        
    def __rotate_left(self, root: Node) -> Node:
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root
    
    def __rotate_right(self, root: Node) -> Node:
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root
    
    def balance(self, root: Node) -> None:
        """
        Balances the tree
        Parameters
        ----------
        root: Node
            root of the tree
        """
        balance_factor = self.__balance_factor(root)
        
        # if tree is left heavy
        if balance_factor > 1:
            if self.__balance_factor(root.left) < 0:
                root.left = self.__rotate_left(root.left)
            root = self.__rotate_right(root)
        
        # if tree is right heavy
        if balance_factor < -1:
            if self.__balance_factor(root.right) > 0:
                root.right = self.__rotate_right(root.right)
            root = self.__rotate_left(root)
            
        self.root = root
                
        