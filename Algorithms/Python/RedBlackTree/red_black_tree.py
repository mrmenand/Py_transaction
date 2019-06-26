RED,BLACK = True,False
class RBTree:
    class _Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.color = RED;

    def __init__(self):
        self._root = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _is_red(self,node):
        if not node:
            return BLACK
        return node.color

    def _left_rotate(self,node):
        """
              node                            x
              /  \          左旋转            / \
             T1   x     ------------>      node T3
                 / \                       /  \
                T2  T3                    T1   T2
        """

        x = node.right
        node.left = x.right
        x.left = node

        x.color = node.color
        node.color = RED

        return x

    def _right_rotate(self,node):
        """
              node                            x
              /  \          右旋转            / \
             x    T2    ------------->      y node
            / \                               /  \
           y  T1                             T1   T2

        """
        x = node.left

        node.left = x.right
        x.right = node

        x.color = node.color
        node.color = RED

        return x


    def  _flip_color(self,node):
        node.color = RED;
        node.left.color = BLACK;
        node.right.color = BLACK;



    def add(self,key,value):
        self._root = self._add(self._root, key, value)
        self._root.color = BLACK

    def _add(self, node, key, value):

        if not node:
            self._size += 1
            return self._Node(key, value)

        if node.key == key:
            node.value = value
        elif node.key > key:
            node.left = self._add(node.left, key, value)
        else:
            node.right = self._add(node.right, key, value)


        if  self._is_red(node.right) and not self._is_red(node.left):
            node = self._left_rotate(node)

        if  self._is_red(node.left) and self._is_red(node.left.left):
            node = self._right_rotate(node)

        if self._is_red(node.left)  and self._is_red(node.right):
            self._flip_color(node)

        return node


    def _get_node(self, node, key):

        if not node:
            return
        if node.key == key:
            return node
        elif node.key > key:
            return self._get_node(node.left, key)
        else:
            return self._get_node(node.right, key)

    def contains(self, key):
        return self._get_node(self._root, key) is not None

    def get(self, key):
        node = self._get_node(self._root, key)
        return node.value if node else None

    def set(self, key, value):
        node = self._get_node(self._root, key)
        if not node:
            raise ValueError(f"{key} doesn't exist")

        node.value = value






