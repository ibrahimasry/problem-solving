from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.mapped = SortedDict()

    def book(self, start: int, end: int) -> bool:
        
        mapped = self.mapped
        if start in mapped:
            mapped[start] += 1
        else :
            mapped[start] = 1
        if end in mapped:
            mapped[end] -= 1
        else :
            mapped[end] = -1
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