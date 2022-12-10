class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        @lru_cache(None)
        def dfs(r, c):
            if c < 0 or c == n: 
                return -1
            if r == m:
                return c
            if c < n - 1:
                if grid[r][c] == 1 and grid[r][c+1] == -1:
                    return -1
            if c > 0:
                if grid[r][c] == -1 and grid[r][c-1] == 1:
                    return -1
            return dfs(r + 1, c + grid[r][c])
        
        
        
        
        
        
        m = len(grid)
        n = len(grid[0])
        res = [-1] * n
        
        for c in range(n):
            res[c] = dfs(0,c)
            
        return res