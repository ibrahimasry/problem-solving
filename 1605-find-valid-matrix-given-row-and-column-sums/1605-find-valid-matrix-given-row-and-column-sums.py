class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        n = len(rowSum)
        m = len(colSum)
        A = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                A[i][j] = min(rowSum[i] , colSum[j])
                rowSum[i] -= A[i][j]
                colSum[j] -= A[i][j]
        return A