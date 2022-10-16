class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events.sort()
        @lru_cache(None)
        def dp(k, i):
            if k == 0 or i == len(events):
                return 0
            
            ans = dp(k, i+1)
            nextI = bisect_left(events, [events[i][1]+1])
            ans = max(ans, dp(k-1, nextI) + events[i][2])
            return ans
        return dp(k, 0)
        