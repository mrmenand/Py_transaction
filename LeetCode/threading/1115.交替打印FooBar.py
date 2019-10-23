# 1115. 交替打印FooBar
import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.sema1 = threading.Semaphore(1)
        self.sema2 = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.sema1.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.sema2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.sema2.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.sema1.release()
