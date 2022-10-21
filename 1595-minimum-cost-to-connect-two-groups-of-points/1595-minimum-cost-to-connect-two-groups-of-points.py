class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        
        
        
        @lru_cache(None)
        def dp(i, mask):
            if i == size1:
                ans2 = 0
                for j in range(size2):
                    if mask & (1 << j) == 0 :
                        ans2 += minCost[j]
                return ans2
            ans = sys.maxsize
            for j in range(size2):
                ans = min(ans, dp(i+1, mask | (1<<j)) + cost[i][j])
            return ans
        
        
        
        
        
        
        
        
        size1 = len(cost)
        size2 = len(cost[0])
        minCost= [sys.maxsize] * size2
        
        
        for i in range(size1):
            for j in range(size2):
                minCost[j] = min(minCost[j], cost[i][j])
        return dp(0,0)
        