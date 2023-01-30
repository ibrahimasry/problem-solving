class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        p = 0
        pp = 1
        ppp = 1
        for j in range(3,n+1):
            curr = p + pp +ppp
            p, pp,ppp = pp, ppp, curr
        return curr