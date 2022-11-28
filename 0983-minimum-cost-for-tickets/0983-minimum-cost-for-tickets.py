class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        
        
        @lru_cache(None)
        def dp(i):
            if i > days[-1]:
                return 0
            if not i in daySet:
                return dp(i+1)
            return min(cost[0] + dp(i+1) , cost[1] + dp(i+7) , cost[2] + dp(i+30))
        daySet = set(days)
        return dp(min(days))
        