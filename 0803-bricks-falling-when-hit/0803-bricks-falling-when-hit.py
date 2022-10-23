class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        
        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < m) :
                return 0

            if grid[i][j] != 1:
                return 0
            res = 1
            grid[i][j] = 2
            res += sum(dfs(x, y) for x, y in dirs(i, j))
            return res
        def connected(i, j):
            return i == 0 or any([ 0 <= x < n and 0 <= y < m and grid[x][y] == 2 for x, y in dirs(i, j)])
        def dirs(i, j):
            return [[i+1,j], [i-1,j], [i,j+1], [i, j-1]]
        n = len(grid)
        m = len(grid[0])
        for i, j in hits:
            grid[i][j] -= 1
        for j in range(m):
            dfs(0, j)

        ans = [0] * len(hits)

        for h in range(len(hits)-1, -1, -1):
            i, j = hits[h]
            grid[i][j] += 1
            if grid[i][j] == 1 and connected(i, j):
                ans[h] = (dfs(i, j) - 1)
        return ans