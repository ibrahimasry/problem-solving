from sortedcontainers import SortedList

class SummaryRanges:

    def __init__(self):
        self.s = SortedList()
    def addNum(self, value: int) -> None:
        self.s.add((value,value))

    def getIntervals(self) -> List[List[int]]:
        curr = self.s
        stack = []
        for s,e in curr:
            if stack and stack[-1][1] + 1 >= s:
                prev = stack.pop()
                stack.append((min(prev[0],s), max(prev[1],e)))
            else :
                stack.append((s,e))
        self.s = SortedList(stack)
        return self.s

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()