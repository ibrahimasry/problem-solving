class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = map(int,date.split("-"))
        over = m-1
        if int(m) > 7:
            over += 1
        over = ceil(over / 2 )
        overFeb = 2 if m > 2 else 0
        over30 = over if m > 1 else 0
        if y != 1900 and m > 2:
            over30 +=  (1 if int(y) % 4 == 0 else 0)
        return 30 * (m - 1) + d - overFeb + over30 
        
