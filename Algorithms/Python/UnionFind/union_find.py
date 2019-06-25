import abc


class UF(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_size(self):
        pass

    @abc.abstractmethod
    def is_connected(self, p, q):
        pass

    @abc.abstractmethod
    def union_element(self, p, q):
        pass


class UnionFind(UF):

    def __init__(self, size):
        self._id = [i for i in range(size)]

    def get_size(self):
        return len(self._id)

    def _find(self, p):
        if p < 0 or p >= self.get_size():
            raise ValueError("p is out of bound")
        return self._id[p]

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union_element(self, p, q):
        p_id = self._find(p)
        q_id = self._find(q)

        if p_id == q_id:
            return

        for i in range(len(self._id)):
            if self._id == p_id:
                self._id[i] = q_id
