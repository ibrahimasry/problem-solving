class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if  i == n-1 and  j == m-1:
                return [grid[-1][-1], grid[-1][-1]]
            if i == n or j == m:
                return [-inf, inf ]
            curr = grid[i][j]
            pos1, neg1 = dp(i+1,j)
            pos2, neg2 = dp(i, j+1)
            mx, mn =  [max(pos1,pos2) * curr , min(neg1, neg2) * curr]
            return [mx, mn] if curr >= 0 else [mn, mx]




        n = len(grid)
        m = len(grid[0])
        
        res = dp(0,0)
        
        pos , neg = res
        return -1 if pos < 0 else pos % (10**9 +7)
            
            