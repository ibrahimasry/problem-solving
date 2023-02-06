class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        @cache
        def dfs(i, j, opened):
            if  i == len(grid) or j == len(grid[0]) or opened < 0:
                return False
            if i == len(grid) - 1 and j == len(grid[0]) -1:
                return opened == 1 and grid[i][j] == ')'

            curr = (-1 if grid[i][j] == ")" else 1)
            return dfs(i+1,j, opened + curr)   or dfs(i,j+1,opened + curr)       
        return dfs(0,0,0)