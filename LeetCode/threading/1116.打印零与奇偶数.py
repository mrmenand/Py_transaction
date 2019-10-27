# 1116. 打印零与奇偶数
import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.z = threading.Semaphore(1)
        self.e = threading.Semaphore(0)
        self.o = threading.Semaphore(0)



    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.z.acquire()
            printNumber(0)
            self.e.release() if i % 2 else self.o.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.e.acquire()
            printNumber(i)
            self.z.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.o.acquire()
            printNumber(i)
            self.z.release()
