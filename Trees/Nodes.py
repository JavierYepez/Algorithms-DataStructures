"""
This module contains all types of nodes needed to build the trees.
"""


class BNode:
    """
    A simple node for a binary tree.
    It has two childs nodes (left and right) and a value field.
    """

    def __init__(self, value):
        """Creates a BNode and sets the value of the node"""
        self.left = None
        self.right = None
        self.value = value
