class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        
        n = len(stones)
        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            res = -sys.maxsize
            for k in range(1,4):
                res = max(res, sum(stones[i:i+k]) - dp(i+k))
            return res
        res = dp(0)
        if res > 0:
            return "Alice"
        if res < 0:
            return "Bob"
        return "Tie"