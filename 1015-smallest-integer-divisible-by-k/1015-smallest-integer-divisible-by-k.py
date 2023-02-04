class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        seen  = set()
        r = 0
        for i in range(k+1):
            rr = r * 10 + 1
            rr %= k
            r= rr
            if rr == 0:
                return i+1
            if rr in seen:
                return -1
            seen.add(rr)