class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        if grid[0][0] == ')':
            return False
        cache = dict()
        def dfs(i, j, opened):
            nonlocal cache
            if  i == len(grid)    or j == len(grid[0]) or opened < 0:
                return False
            if i == len(grid) - 1 and j == len(grid[0]) -1:
                if opened == 1 and grid[i][j] == ')':
                    return True
                return False
                    
            if (i,j,opened) in cache:
                return cache[(i,j,opened)]

            curr = (-1 if grid[i][j] == ")" else 1)
            cache[(i,j,opened)] = dfs(i+1,j,opened + curr)   or dfs(i,j+1,opened + curr)       
            return cache[(i,j,opened)]
        return dfs(0,0,0)