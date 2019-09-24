# 1114. 按序打印
from threading import Barrier


class Foo:
    def __init__(self):
        self.barrier1 = Barrier(2)
        self.barrier2 = Barrier(2)



    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.barrier1.wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.barrier1.wait()
        printSecond()
        self.barrier2.wait()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.barrier2.wait()
        printThird()



# class Foo:
#     def __init__(self):
#         self._first, self._second = None, None
#
#     def first(self, printFirst: 'Callable[[], None]') -> None:
#         # printFirst() outputs "first". Do not change or remove this line.
#         printFirst()
#         self._first = True
#
#     def second(self, printSecond: 'Callable[[], None]') -> None:
#         # printSecond() outputs "second". Do not change or remove this line.
#         while not self._first:
#             pass
#         printSecond()
#         self._second = True
#
#     def third(self, printThird: 'Callable[[], None]') -> None:
#         # printThird() outputs "third". Do not change or remove this line.
#         while not self._second:
#             pass
#         printThird()
