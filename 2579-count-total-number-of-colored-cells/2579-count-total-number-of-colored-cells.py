class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        return 1 + (n-1) * (8 + (n-2) * 4)//2