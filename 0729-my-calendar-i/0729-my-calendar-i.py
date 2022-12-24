from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.books = SortedList()

    def book(self, start: int, end: int) -> bool:
        books = self.books
        idx = bisect.bisect_left(books , start+1 , key=lambda x:x[1])
        if idx == len(self.books) or books[idx][0] >= end :
            books.add((start,end))
            return True
        return False
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)