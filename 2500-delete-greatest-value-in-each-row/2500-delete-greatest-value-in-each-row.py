class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort(reverse=True)
        res = 0
        for col in zip(*grid):
            res += max(col)
        return res