class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        
        
        def dp(r, c1, c2):
            if r == n :
                return 0
            if (r, c1, c2) in memo:
                return memo[(r, c1, c2)]
            cherries = grid[r][c1] + (0 if c1 == c2 else grid[r][c2])
            ans = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nextI = c1 + i
                    nextJ = c2 + j
                    if 0 <= nextI < m  and 0 <= nextJ < m:
                        ans = max(dp(r+1, nextI, nextJ) , ans)
            memo[(r, c1, c2)] = cherries + ans
            return cherries + ans
            
        n = len(grid)
        m = len(grid[0])
        memo = defaultdict(tuple)

        return dp(0, 0, m-1)