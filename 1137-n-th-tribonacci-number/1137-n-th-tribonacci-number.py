class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return (n+1)//2
        
        p = 0
        pp = 1
        ppp = 1
        for j in range(3,n+1):
            p, pp, ppp = pp, ppp, p + pp + ppp
        return ppp