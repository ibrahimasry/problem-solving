class Solution:
    def minDays(self, n: int) -> int:
    
        @lru_cache(None)
        def dp(n):
            if n < 2:
                return n
            ans = 1 + min(n % 3 + dp(n//3), n % 2 + dp(n//2))
            return ans
        return dp(n)
        