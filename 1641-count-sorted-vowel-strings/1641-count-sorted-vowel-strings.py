class Solution:
    def countVowelStrings(self, n: int) -> int:
        values = {  c:i      for i, c in enumerate(["a","e","i","o","u"])}
        @lru_cache(None)
        def dp(curr, prev):
            if curr == 0:
                return 1
            
            res = 0
            
            for c in range(prev, 5):
                res += dp(curr - 1, c)
            return res
        return dp(n, 0)