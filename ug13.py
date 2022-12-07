class Node:
    def __init__(self, data, parent):
        self._data = data
        self._parent = parent
        self._left = None
        self._right = None

    def insert(self, data):
        if data < self.getData():
            if self.left() is None:
                self._left = Node(data, self)
            else:
                self.left().insert(data)
        elif data > self.getData():
            if self.right() is None:
                self._right = Node(data, self)
            else:
                self.right().insert(data)
        else:
            return False
        return True 

    def getData(self):
        return self._data

    def left(self):
        return self._left

    def right(self):
        return self._right

    def parent(self):
        return self._parent

    def isRoot(self):
        return self._parent is None

    def isExternal(self):
        return self._left is None and self._right is None

class BinaryTree:
    def __init__(self):
        self._root = Node(0,None)
        self._size = 0

    def add(self, data):
        if self._root._left is None and data % 2 != 0:
            self._root._left = Node(data,self._root)
        elif self._root._right is None and data % 2 == 0:
            self._root._right = Node(data,self._root)
        else:
            if data % 2 != 0:
                self._root._left.insert(data)
            else:
                self._root._right.insert(data)

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def nodes(self):
        self.inorder(self._root)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left())
            print(node.getData(), end= ' ')
            self.inorder(node.right())

tree = BinaryTree()
tree.add(5)
tree.add(4)
tree.add(3)
tree.add(9)
tree.add(8)
tree.add(6)
tree.add(7)
tree.add(11)
tree.add(10)
tree.nodes()