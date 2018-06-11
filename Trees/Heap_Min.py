
class MinHeap:
    """A heap which has the minimum value at the root.
    """

    def __init__(self):
        """Creates an empty heap.

        Return: MinHeap
        """
        self.heap = []

    def peek(self):
        """Gets the root value (the minimum).

        Return: value
        """
        if self.heap:
            return self.heap[0]
        else:
            raise IndexError("there is no root")

    def extractMin(self):
        """Gets the root value (the minimum) and removes it.

        Return: value
        """
        if not self.heap:
            raise IndexError("there is no root")
        elif len(self.heap) < 2:
            return self.heap.pop()
        else:
            self.heap[0], oldMin = self.heap.pop(), self.heap[0]
            self._shiftDown()
            return oldMin

    def insert(self, value):
        """Inserts a value to the heap.

        Return: None
        """
        self.heap.append(value)
        self._shiftUp()

    def _shiftUp(self):
        index = len(self.heap) - 1
        while self._hasParent(index) and \
                self._getParent(index) > self.heap[index]:
            parentIndex = self._getParentIndex(index)
            self.heap[index], self.heap[parentIndex] = \
                self.heap[parentIndex], self.heap[index]
            index = parentIndex

    def _shiftDown(self):
        index = 0
        while self._hasLeftChild(index):
            minChildIndex = self._getLeftChildIndex(index)
            if self._hasRightChild(index) and \
                    self._getLeftChild(index) > self._getRightChild(index):
                minChildIndex = self._getRightChildIndex(index)

            if self.heap[index] < self.heap[minChildIndex]:
                break
            else:
                self.heap[index], self.heap[minChildIndex] = \
                    self.heap[minChildIndex], self.heap[index]
            index = minChildIndex

    # The calculations to get the index of the nodes

    def _getLeftChildIndex(self, parentIndex):
        return 2*parentIndex+1

    def _getRightChildIndex(self, parentIndex):
        return 2*parentIndex+2

    def _getParentIndex(self, childIndex):
        return int((childIndex - 1) / 2)

    def _getLeftChild(self, parentIndex):
        return self.heap[2*parentIndex+1]

    def _getRightChild(self, parentIndex):
        return self.heap[2*parentIndex+2]

    def _getParent(self, childIndex):
        return self.heap[int((childIndex - 1) / 2)]

    def _hasLeftChild(self, parentIndex):
        return 2*parentIndex+1 < len(self.heap)

    def _hasRightChild(self, parentIndex):
        return 2*parentIndex+2 < len(self.heap)

    def _hasParent(self, childIndex):
        return int((childIndex - 1) / 2) >= 0


if __name__ == '__main__':
    heap = MinHeap()

    heap.insert(5)
    heap.insert(8)
    heap.insert(9)
    heap.insert(15)
    heap.insert(2)

    print("min value: {}".format(heap.peek()))

    print("old: {} new: {}".format(heap.extractMin(), heap.peek()))
