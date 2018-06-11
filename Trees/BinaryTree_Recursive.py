
from Nodes import BNode as Node


class BinaryTree:
    """A type tree which has as much as two children nodes per node.
    """

    def __init__(self):
        """Creates a binary tree without nodes. 

        Return: BinaryTree
        """
        self.root = None

    def add(self, value):
        """Adds a node in the tree with the given value.

        Return: None
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value):
        """Finds the node with the given value in the tree.

        Return: BNode
        """
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value:
            if node.left is None:
                return None
            else:
                return self._find(value, node.left)
        else:
            if node.right is None:
                return None
            else:
                return self._find(value, node.right)

    def minValueNode(self, node=None):
        """Search the node with the lowest value.

        Return: BNode
        """
        if node is None:
            current = self.root
        else:
            current = node
        while current.left is not None:
            current = current.left

        return current

    def clearTree(self):
        """Remove all the nodes of the tree.

        Return: None
        """
        self.root = None

    def removeNode(self, value):
        """Removes the node in the tree with the given value if it exists.

        Return: None
        """
        self.root = self._removeNode(self.root, value)

    def _removeNode(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._removeNode(node.left, value)
        elif(value > node.value):
            node.right = self._removeNode(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.minValueNode(node.right)
            node.value = temp.value
            node.right = self._removeNode(node.right, temp.value)

        return node

    def printInorder(self):
        """Prints the tree inorder (left, root, right) on stdout.

        Return: None
        """
        if self.root is not None:
            self._printInorder(self.root)

    def _printInorder(self, node):
        if node is not None:
            self._printInorder(node.left)
            print("{} ".format(node.value), end='')
            self._printInorder(node.right)


# Test the tree
if __name__ == '__main__':
    tree = BinaryTree()

    tree.add(50)
    tree.add(30)
    tree.add(20)
    tree.add(40)
    tree.add(70)
    tree.add(60)
    tree.add(80)

    tree.printInorder()
    node = tree.find(50)

    tree.removeNode(30)
    tree.printInorder()

    print("\n"+str(tree.minValueNode().value))
