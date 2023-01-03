class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        @cache
        def dp(n,k):
            if n == k:
                return 1
            if n == 0 or k == 0:
                return 0
            return dp(n-1,k) * (n-1)  % (10 ** 9 + 7) + dp(n-1,k-1)  % (10 ** 9 + 7)
        return dp(n,k) % (10 ** 9 + 7)