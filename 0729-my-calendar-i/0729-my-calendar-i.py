from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.books = SortedList()

    def book(self, start: int, end: int) -> bool:
        books = self.books
        idx = self.bst(self.books, start)
        if idx == len(self.books) :
        
            books.add((start,end))
            return True
        if self.books[idx][0] >= end:
            books.add((start,end))
            return True
        return False
    def bst(self ,books, start):
        l = 0
        r = len(books)
        while l < r:
            m = l + (r-l)//2
            if books[m][1] > start:
                r = m 
            else :
                l = m + 1
        return l
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)