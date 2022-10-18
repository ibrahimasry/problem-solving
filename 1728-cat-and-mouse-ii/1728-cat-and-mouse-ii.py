class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        
        @lru_cache(None)
        def dp(mouse, cat , moves):
            if mouse == cat:
                return False
            if cat == food:
                return False
            if mouse == food:
                return True
            if moves == available * 2:
                return False
            if moves % 2 == 0 :
                for [x, y] in dirs:
                    for l in range(mouseJump + 1):
                        nx = mouse[0] + (x * l)
                        ny = mouse[1] + (y * l)
                        
                        if  n > nx >= 0 and m > ny >= 0 and grid[nx][ny] != "#":
                            if dp((nx, ny), cat, moves + 1):
                                return True
                        else :
                            break
                return False
            else :
                for [x, y] in dirs:
                    for l in range(catJump + 1):
                        nx = cat[0] + (x * l)
                        ny = cat[1] + (y * l)
                        
                        if  n > nx >= 0 and m > ny >= 0 and grid[nx][ny] != "#":
                            if not dp(mouse, (nx, ny), moves + 1):
                                return False
                        else :
                            break
                return True
            
        n = len(grid)
        m = len(grid[0])
        food = cat = mouse = None
        available = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "C":
                    cat = (i, j)
                if grid[i][j] == "F":
                    food = (i,j)
                if grid[i][j] == "M":
                    mouse = (i,j)
                if grid[i][j] != '#':
                     available += 1
        dirs = [[0,1], [-1,0], [1,0],[0,-1]]
    
        return dp(mouse, cat, 0)
                