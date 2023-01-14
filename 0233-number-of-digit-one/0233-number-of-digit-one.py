class Solution:
    def countDigitOne(self, n: int) -> int:
        q = n
        ans = 0
        base = 1
        while base <= n:
            curr = n // base % 10
            left = n //  base // 10
            right = n % base 
            if curr > 1:
                ans += (left + 1) * base 
            if curr == 1:
                ans += (left * base) + right + 1
            if curr < 1:
                ans += left * base
            base *= 10
        return ans