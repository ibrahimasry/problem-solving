class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dp(i, t, p):
            if i == m:
                if t == 0:
                    return 0
                return inf
            ans = inf
            
            if houses[i]:
                return dp(i+1, t - (houses[i] != p) , houses[i])
            return min([dp(i+1, t - (k+1 != p) , k+1) + cost[i][k] for k in range(n)])
        res =  dp(0,target, -1)             
        return -1 if res == inf else res