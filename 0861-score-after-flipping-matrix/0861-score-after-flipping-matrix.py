class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        n = len(grid[0])
        m = len(grid)
        
        res = (1 << (n-1)) * m
        
        for c in range(1,n):
            curr = 0
            for r in range(m):
                curr += 1 if grid[r][c] == grid[r][0] else 0
            res += max(curr, m - curr) * ( 1 << (n-c-1))
        return res