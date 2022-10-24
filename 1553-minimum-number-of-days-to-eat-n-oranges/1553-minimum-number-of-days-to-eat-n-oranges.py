class Solution:
    def minDays(self, n: int) -> int:
    
        @lru_cache(None)
        def dp(n):
            return n if n < 2 else 1 + min(n % 3 + dp(n//3), n % 2 + dp(n//2))
        return dp(n)
        