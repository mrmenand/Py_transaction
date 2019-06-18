from random import randint


class BST:
    class _Node:

        def __init__(self, e):
            self.e = e
            self.left = None
            self.right = None

    def __init__(self):
        self._root = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, e):
        self._root = self._add(self._root, e)

    def _add(self, node, e):
        if not node:
            self._size += 1
            return self._Node(e)

        if node.e == e:
            return node
        elif node.e > e:
            node.left = self._add(node.left, e)
        else:
            node.right = self._add(node.right, e)

        return node

    def contains(self, e):
        return self._contains(self._root, e)

    def _contains(self, node, e):
        if not node:
            return False
        if node.e == e:
            return True
        elif node.e > e:
            return self._contains(node.left, e)
        else:
            return self._contains(node.right ,e)

    def pre_order(self):
        self._pre_order(self._root)

    def _pre_order(self, node):
        if not node:
            return
        print(node.e,end=" ")
        self._pre_order(node.left)
        self._pre_order(node.right)

    def pre_orderNR(self):
        stack = [self._root]
        while stack:
            cur = stack.pop()
            print(cur.e, end= " ")
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)


    def in_order(self):
        self._in_order(self._root)

    def _in_order(self, node):
        if not node:
            return
        self._pre_order(node.left)
        print(node.e, end=" ")
        self._pre_order(node.right)

    def post_order(self):
        self._post_order(self._root)

    def _post_order(self, node):
        if not node:
            return
        self._pre_order(node.left)
        self._pre_order(node.right)
        print(node.e, end=" ")


    def level_order(self):
        stack = [self._root]
        while stack:
            cur = stack.pop(0)
            print(cur.e, end=" ")
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

    def mininum(self):
        if self.is_empty():
            raise ValueError("Empty BST")
        self._mininum(self._root)

    def _mininum(self, node):
        if not node.left:
            return node
        return self._mininum(node.left)

    def maxnum(self):
        if self.is_empty():
            raise ValueError("Empty BST")
        self._maxnum(self._root)

    def _maxnum(self, node):
        if not node.right:
            return node
        return self._maxnum(node.right)

    def remove_min(self):
        ret = self.mininum()
        self._root  = self._remove_min(self._root)
        return ret

    def _remove_min(self, node):
        if not node.left:
            rightnode = node.right
            node.right = None
            self._size -= 1
            return rightnode
        node.left =  self._remove_min(node.left)
        return node

    def remove_max(self):
        ret = self.maxnum()
        self._root = self._reove_max(self._root)
        return ret

    def _reove_max(self, node):
        if not node.right:
            leftnode = node.left
            node.left = None
            self._size -= 1
            return leftnode
        node.right = self._reove_max(node.right)
        return node

    def   remove(self,e):
        self._root = self._remove(self._root,e)

    def _remove(self, node, e):
        if not node:
            return

        if node.e > e :
            node.left = self._remove(node.left,e)
            return node
        elif node.e < e:
            node.right = self._remove(node.right,e)
            return node
        else:
            if not node.left:
                rightnode= node.right
                node.right = None
                self._size -= 1
                return rightnode
            if not node.right:
                leftnode= node.left
                node.left = None
                self._size -= 1
                return leftnode
            successor = self._mininum(node.right)
            successor.right = self._remove_min(node.right)
            successor.left = node.left

            node.left = node.right = None
            return successor

    def _generate_depth_string(self,depth):
        res =""
        for _ in range(depth):
            res += "--"
        return res

    def _generate_BST_string(self,node,depth,res):
        if not node:
            res.append(self._generate_depth_string(depth) + "None \n")
            return

        res.append(self._generate_depth_string(depth) + str(node.e) + "\n")
        self._generate_BST_string(node.left,depth+1,res)
        self._generate_BST_string(node.right,depth +1 ,res)

    def __str__(self):
        res = []
        self._generate_BST_string(self._root,0,res)
        return "BST : \n " + "".join(res)



if __name__ == '__main__':
    bst = BST()

    for _ in range(10):
        bst.add(randint(10,66))

    print(bst)
    bst.pre_orderNR()
    print("\n"+"*" * 20)
    bst.level_order()









