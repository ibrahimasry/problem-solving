class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while n != 1:
            if n % 2:
                if n == 3 or bin(n-1).count("1") < bin(n+1).count("1"):
                    n -= 1
                    res += 1
                else :
                    n += 1
                    res += 1
            n = n // 2
            res += 1
        return res