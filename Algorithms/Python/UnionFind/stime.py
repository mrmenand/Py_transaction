from random import randint
from time import time

from UnionFind.union_find import UnionFind
from UnionFind.union_find2 import UnionFind2
from UnionFind.union_find3 import UnionFind3
from UnionFind.union_find4 import UnionFind4
from UnionFind.union_find5 import UnionFind5
from UnionFind.union_find6 import UnionFind6

def stime(uf,m):
    size = uf.get_size()
    start_time = time()

    for _ in range(m):
        a = randint(0,size-1)
        b = randint(0,size-1)
        uf.union_element(a,b)

    for _ in range(m):
        a = randint(0, size - 1)
        b = randint(0, size - 1)
        uf.is_connected(a,b)

    end_time = time()

    print(f"Time cost :  {end_time-start_time} s")


class UnionFind1(object):
    pass


if __name__ == '__main__':
    size = 10000
    m = 10000

    uf1 = UnionFind(size)
    stime(uf1,m)

    uf2 = UnionFind2(size)
    stime(uf2,m)

    uf3 = UnionFind3(size)
    stime(uf3,m)

    uf4 = UnionFind4(size)
    stime(uf4,m)

    uf5 = UnionFind5(size)
    stime(uf5,m)

    uf6 = UnionFind6(size)
    stime(uf6,m)




