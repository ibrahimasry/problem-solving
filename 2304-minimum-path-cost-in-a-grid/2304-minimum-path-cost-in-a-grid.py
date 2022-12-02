class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        @lru_cache(None)
        def dfs (r, c):
            if r == len(grid) - 1:
                return grid[r][c]
            minn = sys.maxsize
            for j in range(len(grid[0])):
                minn = min(minn, dfs(r+1, j) + moveCost[grid[r][c]][j] + grid[r][c])
            return minn

        minn = sys.maxsize
        for i in range(len(grid[0])):
            minn = min(dfs(0, i), minn)
            
            
        return minn
