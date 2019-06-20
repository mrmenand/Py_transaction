from Arrays.queue import Queue
from Heap.max_heap import MaxHeap


class PriorityQueue(Queue):

    def __init__(self):
        self._max_heap = MaxHeap()

    def get_size(self):
        return self._max_heap.size()

    def is_empty(self):
        return self._max_heap.is_empty()

    def get_font(self):
        return self._max_heap.find_max()

    def enqueue(self, e):
        return self._max_heap.add(e)

    def dequeue(self):
        return self._max_heap.extract_max()


