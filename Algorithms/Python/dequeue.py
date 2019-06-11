class Deque(object):
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self,item):
        """头部入"""
        self.__list.insert(0,item)

    def add_rear(self,item):
        """尾部入"""
        self.__list.append(item)

    def pop_front(self):
        """头部取"""
        return  self.__list.pop(0)

    def pop_rear(self):
        """尾部取"""
        return self.__list.pop()

    def is_empty(self):
        """"判空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)

if __name__ == '__main__':
    s = Deque()
    s.add_rear(1)
    s.add_rear(2)
    s.add_rear(3)
    s.add_rear(6)
    s.add_front(4)
    print(s.pop_front())
    print(s.pop_rear())
