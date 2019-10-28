# 1195. 交替打印字符串
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.d = {}

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        self.d["f"] = printFizz
        self._check()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        self.d["b"] = printBuzz
        self._check()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        self.d["fb"] = printFizzBuzz
        self._check()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        self.d["n"] = printNumber
        self._check()

    def _check(self):
        if len(self.d) == 4:
            for i in range(1, self.n + 1):
                if i % 15 == 0:
                    self.d["fb"]()
                elif i % 3 == 0:
                    self.d["f"]()
                elif i % 5 == 0:
                    self.d["b"]()
                else:
                    self.d["n"](i)






