from .Node import Node


class BinaryTree:
    """
    Create a binary tree object.
    """

    def __init__(self, root: any = None):
        """
        Parameters
        ----------
        root : Node
            The root node of the tree.
        """
        if root == None:
            self.root = root
        else:
            self.root = Node(root)
            
        self.inorderView = []
        self.preorderView = []
        self.postorderView = []

    def __str__(self) -> str:
        """
        Return a string representation of the tree.
        """
        return self.__str_repr(self.root, "")
    
    
    def __str_repr(self, node, indent):
        if node is None:
            return ""
        return f"{indent}{node.value}\n" + self.__str_repr(node.left, indent + "left ") + self.__str_repr(node.right, indent + "right ")


    def get_root(self) -> Node:
        """
        Return the root node of the tree.
        """
        return self.root
    
    def insert(self, value: any):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__insert_helper(self.root, value)
            
            
    def __insert_helper(self, node: Node, value: any):
        if node.left is None:
            node.left = Node(value)
        elif node.right is None:
            node.right = Node(value)
        else:
            self.__insert_helper(node.left, value)
            
    def search(self, value: any):
        current = self.root
        
        if current is not None:
            if current.value == value:
                return current
        
            # searching left
            if current.left is not None:
                if current.left.value == value:
                    return current.left
                else:
                    current = current.left
                    return self.__search_helper(current, value, left=True)
            
            
            # searching right
            if current.right is not None:
                if current.right.value == value:
                    return current.right
                elif current.right:
                    current = current.right
                    return self.__search_helper(current, value, left=False)

        
        
    def __search_helper(self, node: Node, value: any, left: bool):
        if left:
            if node.left is None:
                return None
            elif node.left.value == value:
                return node.left
            else:
                return self.__search_helper(node.left, value, left)
        else:
            if node.right is None:
                return None
            elif node.right.value == value:
                return node.right
            else:
                return self.__search_helper(node.right, value, left)
            
            
    def delete(self, value: any):
        current = self.root
        if current is not None:
            if current.value == value:
                self.root = None
                return current
            
            # searching left
            if current.left is not None:
                if current.left.value == value:
                    current.left = None
                    return current.left
                else:
                    current = current.left
                    return self.__delete_helper(current, value, left=True)
            
            
            # searching right
            if current.right is not None:
                if current.right.value == value:
                    current.right = None
                    return current.right
                elif current.right:
                    current = current.right
                    return self.__delete_helper(current, value, left=False)
                
                
    def __delete_helper(self, node: Node, value: any, left: bool):
        if left:
            if node.left is None:
                return None
            elif node.left.value == value:
                node.left = None
                return node.left
            else:
                return self.__delete_helper(node.left, value, left)
        else:
            if node.right is None:
                return None
            elif node.right.value == value:
                node.right = None
                return node.right
            else:
                return self.__delete_helper(node.right, value, left)
            
            
            
    def inorder(self):
        return self.__inorder_helper(self.root)
    
    
    def __inorder_helper(self, root: Node):
        if root:
            self.__inorder_helper(root.left)
            self.inorderView.append(root.value)
            self.__inorder_helper(root.right)
            
        return self.inorderView
    
    def preorder(self):
        return self.__preorder_helper(self.root)
    
    def __preorder_helper(self, root: Node):
        if root:
            self.preorderView.append(root.value)
            self.__preorder_helper(root.left)
            self.__preorder_helper(root.right)
            
        return self.preorderView
    
    def postorder(self):
        return self.__postorder_helper(self.root)
    
    
    def __postorder_helper(self, root: Node):
        if root:
            self.__postorder_helper(root.left)
            self.__postorder_helper(root.right)
            self.postorderView.append(root.value)
            
        return self.postorderView
    
    
    def height(self):
        return self.__height_helper(self.root)
    
    def __height_helper(self, root):
        if root is None:
            return 0
        else:
            left_height = self.__height_helper(root.left)
            right_height = self.__height_helper(root.right)
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1
            
            
    def size(self):
        return self.__size_helper(self.root)
    
    def __size_helper(self, root):
        if root is None:
            return 0
        else:
            return self.__size_helper(root.left) + 1 + self.__size_helper(root.right)
        
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
        
    def max(self):
        return self.__max_helper(self.root)
    
    
    def __max_helper(self, root):
        if root is None:
            return float("-inf")
        else:
            return max(root.value, self.__max_helper(root.left), self.__max_helper(root.right))
        
        
    def min(self):
        return self.__min_helper(self.root)
    
    
    def __min_helper(self, root):
        if root is None:
            return float("+inf")
        else:
            return min(root.value, self.__min_helper(root.left), self.__min_helper(root.right))