from sortedcontainers import SortedList
class CountIntervals:

    def __init__(self):
        self.a = SortedList()
        self.c = 0
        

    def add(self, left: int, right: int) -> None:
        def overlap(x,y, x1,y1):
            return  x1 <= y and y1 >= x
        a = self.a
        if a:
            i = bisect.bisect_left(a, (left,-1))
            j = i
            if j > 0 and a[j-1][1] >= left:
                j -= 1
                left = min(left, a[j][0])
                right = max(right , a[j][1])


            while i < len(a) and overlap(left,right, *a[i]):
                right = max(right , a[i][1])
                i += 1



            for k in range(j, i):
                self.c -= ((a[k][1] - a[k][0]) + 1)
            del a[j:i]

        self.c += ((right - left) + 1)
        a.add((left,right))

    def count(self) -> int:
        return self.c


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()