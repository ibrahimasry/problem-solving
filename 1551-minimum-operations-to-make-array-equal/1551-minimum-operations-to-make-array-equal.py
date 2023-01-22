class Solution:
    def minOperations(self, n: int) -> int:
        m = (n // 2) * 2 + 1
        m -= n % 2 == 0
        res = 0
        for i in range(n//2 ):
            res += m - (i*2 + 1)
        return res