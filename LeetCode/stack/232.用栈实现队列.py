class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return
        else:
            return self.queue.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return len(self.queue) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()