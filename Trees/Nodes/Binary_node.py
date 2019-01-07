
class binary_node:
    """
    A simple node for a binary tree.
    It has two childs nodes (left and right) and a value field.
    """

    def __init__(self, value):
        """Creates a Binary_node and sets the value of the node"""
        self.left = None
        self.right = None
        self.value = value
