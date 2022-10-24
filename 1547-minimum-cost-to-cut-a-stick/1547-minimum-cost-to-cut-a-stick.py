class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        @lru_cache(None)
        def dp(start, end):
            ans = sys.maxsize
            for cut in cuts:
                if  start < cut < end:
                    ans = min(ans, (dp(start, cut) + dp(cut, end) + (end - start)))
            if ans == sys.maxsize :
                return 0
            return ans
        return dp(0, n)