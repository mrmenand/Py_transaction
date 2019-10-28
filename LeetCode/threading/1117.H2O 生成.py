# 1117. H2O 生成
class H2O:
    def __init__(self):
        self.h = []
        self.o  = []

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.h.append(releaseHydrogen)
        self.queue()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.o.append(releaseOxygen)
        self.queue()

    def queue(self):
        if len(self.h) > 1 and len(self.o) :
            self.h.pop()()
            self.h.pop()()
            self.o.pop()()
