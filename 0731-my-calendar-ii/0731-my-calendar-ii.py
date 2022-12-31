from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.mapped = SortedDict(defaultdict(lambda:0))

    def book(self, start: int, end: int) -> bool:
        
        mapped = self.mapped
        mapped[start] =  mapped[start] + 1 if start in mapped else 1
        mapped[end]   =   mapped[end] - 1 if end in mapped else -1
        overlapped = 0
        
        for  val in mapped.values():
            overlapped += val
            if overlapped == 3:
                mapped[start] -= 1
                mapped[end] += 1
                return False
        
        
        return True
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)