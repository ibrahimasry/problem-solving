class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        @lru_cache(None)
        def dp(x, y, x2):
            y2 = x + y - x2
            if x == n-1 and y == n-1:
                if grid[x][y] == -1:
                    return -sys.maxsize
                return grid[x][y]
            if n <= x  or n <= y  or n <= x2   or n <= y2  or grid[x][y] == -1 or grid[x2][y2] == -1:
                return -sys.maxsize

            curr = grid[x][y] + grid[x2][y2]
            if (x,y) == (x2,y2) and curr > 0:
                curr -= grid[x][y]
            
            res = max(dp(x+1,y,x2+1) , dp(x,y+1, x2+1) , dp(x, y+1, x2) , dp(x+1, y, x2))
            return curr + res
        n = len(grid)
        res = dp(0, 0, 0)
        if res > 0:
            return res
        return 0