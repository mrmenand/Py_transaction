from UnionFind.union_find import UF


class UnionFind2(UF):

    def __init__(self, size):
        self._parent = [i for i in range(size)]

    def get_size(self):
        return len(self._parent)

    def _find(self, p):
        if p < 0 or p >= self.get_size():
            raise ValueError("p is out of bound")

        while p != self._parent[p]:
            p = self._parent[p]

        return p

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union_element(self, p, q):
        p_root = self._find(p)
        q_root = self._find(q)

        if q_root == p_root:
            return

        self._parent[p_root] = q_root
