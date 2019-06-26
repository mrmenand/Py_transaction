
class AVLTree:

    class _Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self._root = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_balanced(self):
        return self._is_balanced(self._root)

    def _is_balanced(self, node):

        if not node:
            return True

        balance_factor = self._get_balance_factor(node)
        if balance_factor > 1:
            return False
        return self.is_balanced(node.left) and self.is_balanced(node.right)

    def _get_balance_factor(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def is_bst(self):

        keys = []
        self._in_order(self._root, keys)
        for i in range(1, len(keys)):
            if keys[i - 1] > keys[i]:
                return False
        return True

    def _in_order(self, node, keys):
        if not node:
            return

        self._in_order(node.left, keys)
        keys.append(node.key)
        self._in_order(node.right, keys)

    def _right_rotate(self, y):
        """
              对节点y进行向右旋转操作，返回旋转后的新的根节点x
                      y                                 x
                     / \                               / \
                    x   T4      向右旋转 (y)           z    y
                   / \        -------------->       / \   / \
                  z   T3                           T1 T2 T3  T4
                 / \
                T1  T2
        """
        x = y.left
        t3 = x.right

        x.right = y
        y.left = t3

        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right))

        return x

    def _left_rotate(self, y):
        """
             对节点y进行向左旋转操作，返回旋转后的新的根节点x
                  y                                 x
                 / \                               / \
                T1  x      向右旋转 (y)            y    z
                   / \     -------------->      / \   / \
                  T2  z                        T1 T2 T3  T4
                     / \
                    T1 T2
             """

        x = y.right
        t2 = x.left

        x.left = y
        y.right = t2

        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right))

        return x

    def add(self, key, value):
        self._root = self._add(self._root, key, value)

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

        node.height = max(
            self._get_height(
                node.left), self._get_height(
                node.right)) + 1

        balance_factor = self._get_balance_factor(node)

        # LL
        if balance_factor > 1 and self._get_balance_factor(node.left) >= 0:
            return self._right_rotate()

        # LR

        if balance_factor > 1 and self._get_balance_factor(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # RR
        if balance_factor < -1 and self._get_balance_factor(node.right) <= 0:
            return self._left_rotate(node)

        # RL
        if balance_factor < -1 and self._get_balance_factor(node.right) > 0:
            node.right = self._right_rotate(node.right)

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

    def minimum(self):
        if self.is_empty():
            raise ValueError("AVLTree is empty")
        self._minimum(self._root)

    def _minimum(self, node):
        if not node.left:
            return node
        return self._minimum(node.left)

    def remove(self, key):
        node = self._get_node(self._root, key)
        if not node:
            self._root = self._remove(self._root, key)
            return node.value

    def _remove(self, node, key):

        if not node:
            return

        if node.key > key:
            node.left = self._remove(node.left, key)
            ret_node = node

        elif node.key < key:
            node.right = self._remove(node.right, key)
            ret_node = node
        else:
            if not node.left:
                right_node = node.right
                node.right = None
                self._size -= 1
                ret_node = right_node

            elif not node.right:
                left_node = node.left
                node.left = None
                self._size -= 1
                ret_node = left_node

            else:
                successor = self.minimum(node.right)
                successor.right = self._remove(node.right, successor.key)
                successor.left = node.left

                node.left = node.right = None
                ret_node = successor

        if not ret_node:
            return

        ret_node.height = max(
            self._get_height(
                ret_node.left), self._get_height(
                ret_node.right)) + 1
        balance_factor = self._get_balance_factor(node)

        # LL
        if balance_factor > 1 and self._get_balance_factor(ret_node.left) >= 0:
            return self._right_rotate()

        # LR

        if balance_factor > 1 and self._get_balance_factor(ret_node.left) < 0:
            ret_node.left = self._left_rotate(ret_node.left)
            return self._right_rotate(ret_node)

        # RR
        if balance_factor < - \
                1 and self._get_balance_factor(ret_node.right) <= 0:
            return self._left_rotate(ret_node)

        # RL
        if balance_factor < - \
                1 and self._get_balance_factor(ret_node.right) > 0:
            ret_node.right = self._right_rotate(ret_node.right)

        return ret_node

