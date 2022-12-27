class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10
        base = 9
        i = 2
        while i <= n :
            base *= (9-i+2)
            ans += base
            i += 1
        return ans