class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        
        
        h2p = [[] for _ in range(41)]
        n = len(hats)
        
        for  i , curr in enumerate(hats):
            for h in curr:
                h2p[h].append(i)
        @lru_cache(None)
        def dp(h, mask):
            if mask == 2 ** n -1:
                return 1
            if h > 40:
                return 0
            ans = dp(h+1, mask)
            if h2p[h] :
                for i in h2p[h]:
                    if (mask >> i & 1) == 0:
                        ans += dp(h+1, mask | 1 << i)
            return ans
        return dp(1, 0) % (10**9 + 7)
        