from Arrays.array import Array
import abc


class Stack:
    @abc.abstractmethod
    def push(self):
        pass

    @abc.abstractmethod
    def pop(self):
        pass

    @abc.abstractmethod
    def peek(self):
        pass

    @abc.abstractmethod
    def get_size(self):
        pass

    @abc.abstractmethod
    def is_empty(self):
        pass


class ArrayStack(Stack):

    def __init__(self, capacity=0):
        self._array = Array(capacity=capacity)

    def push(self, e):
        self._array.append(e)

    def pop(self):
        return self._array.remove_last()

    def peek(self):
        return self._array.get_last()

    def get_size(self):
        return self._array.get_size()

    def is_empty(self):
        return self._array.get_capacity()

    def get_capacity(self):
        return self._array.get_capacity()

    def __str__(self):
        return str(f"ArrayStack : {self._array}")


if __name__ == '__main__':
    def isValid(s):
        d = {')': '(', '}': '{', ']': '['}
        stack = ArrayStack()
        for c in s:
            if c not in d:
                stack.push(c)
            elif not stack or d[c] != stack.pop():
                return False
        return True

    s1 = "[{(())}]"
    print(isValid(s1))

    s2 = "[}"
    print(isValid(s2))
