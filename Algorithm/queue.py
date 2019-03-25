class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self,item):
        """入队"""
        self.__list.append(item)
        # self.__list.insert(0,item)

    def dequeue(self):
        """出队"""
        return  self.__list.pop(0)
        # return self.__list.pop()
    def is_empty(self):
        """"判空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)

if __name__ == '__main__':
    s = Queue()
    s.enqueue(1)
    s.enqueue(4)
    s.enqueue(6)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())