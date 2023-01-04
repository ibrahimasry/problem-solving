from sortedcontainers import SortedList
class CountIntervals:

    def __init__(self):
        self.a = SortedList()
        self.c = 0
        

    def add(self, left: int, right: int) -> None:
        def overlap(x,y, x1,y1):
            return  x1 <= y and y1 >= x
        if self.a:
            i = bisect.bisect_left(self.a, (left,-1))
            j = i
            if j > 0 and self.a[j-1][1] >= left:
                j -= 1
            while i < len(self.a) and overlap(left,right, *self.a[i]):
                i += 1
            for k in range(j, i):
                left = min(left, self.a[k][0])
                right = max(right , self.a[k][1])

                self.c -= ((self.a[k][1] - self.a[k][0]) + 1)
            del self.a[j:i]

        self.c += ((right - left) + 1)
        self.a.add((left,right))

    def count(self) -> int:
        return self.c


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()