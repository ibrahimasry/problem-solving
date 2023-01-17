class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = date.split("-")
        days = [31,28 , 31,30,31,30,31,31,30,31,30,31]
        if y != "1900":
            days[1] +=  (1 if int(y) % 4 == 0 else 0)
        res = 0
        
        for i in range(int(m)-1):
            res += days[i]
        return res + int(d) 