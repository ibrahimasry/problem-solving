class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        total = sum([abs(c) for row in matrix for c in row])
        neg = [abs(c) for row in matrix  for c in row if c < 0]
        if len(neg) % 2 == 0:
            return total
        return total - 2 * min([abs(c) for r in matrix for c in r])