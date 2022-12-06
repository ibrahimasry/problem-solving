class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        
        n = len(grid[0])
        
        row =[0] * m
        col = [0] * n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    col[j] += 1
                    row[i] += 1
                    
        for i in range(m):
            for j in range(n):
                grid[i][j] = -n -m + 2 * col[j] + 2 * row[i]
        return grid