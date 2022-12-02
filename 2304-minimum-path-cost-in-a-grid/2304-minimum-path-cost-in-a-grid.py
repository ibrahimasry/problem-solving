class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        
        dp = [0] * m
        
        for i in range(m):
            dp[i] = grid[0][i]
            
        for i in range(1, n):
            curr = [sys.maxsize] * m
            for j in range(m):
                for k in range(m):
                    curr[j] = min(curr[j] , dp[k] + moveCost[grid[i-1][k]][j] + grid[i][j])
            dp = curr
        return min(dp)
        
