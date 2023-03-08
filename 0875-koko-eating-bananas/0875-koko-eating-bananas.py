class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def good(t):
            res = 0
            for p in piles:
                res += ceil(p/t)
            return res <= h
        l = 1
        r = sum(piles) + 1
        while l < r:
            m = l + r >> 1
            if good(m):
                r = m
            else :
                l = m + 1
        return l