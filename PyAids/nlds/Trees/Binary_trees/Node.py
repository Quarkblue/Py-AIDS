"""
A node module for binary trees with left and right pointer and a data block
"""


class Node:

    def __init__(self, value: any, left_node: any = None, right_node: any  = None) -> None:
        self.left = left_node
        self.right = right_node
        self.value = value

    def __str__(self) -> str:
        return f"Node({self.value})"

    def __repr__(self) -> str:
        return self.__str__()
