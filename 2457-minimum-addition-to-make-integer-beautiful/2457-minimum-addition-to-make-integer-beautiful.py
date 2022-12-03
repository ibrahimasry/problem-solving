class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        summ = sum([int(c) for c in str(n)])
        ans = 0
        if summ <= target:
            return ans
        i = 0
        source = n
        while sum([int(c) for c in str(n)]) > target:
            i += 1
            n = n // 10
            n += 1
        return n * 10 ** i - source
            