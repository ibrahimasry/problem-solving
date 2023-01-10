class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r = len(grid)
        c = len(grid[0])
        ans = [[0] * c for _ in range(r)]
        for pos in range(r*c):
            i,j = divmod((pos + k) % (c*r), c)
            ans[i][j] = grid[pos//c][pos%c]
        return ans