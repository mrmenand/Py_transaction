# 729. 我的日程安排表 I
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:

        for booking in self.calendar:
            if start >= booking[1] or end <= booking[0]:
                pass
            else:
                return False

        self.calendar.append([start,end])
        return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
