class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        arr = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                arr[i][j] = -arr[i-1][j-1] + arr[i-1][j] + arr[i][j-1] + mat[i-1][j-1]
        ans = [[0] * n for _ in range(m)]
        
        for r in range(1,m+1):
            for c in range(1, n+1):
                r2 = min(r + k,m) 
                r1 = max(r - k,1)
                c1 = max(c - k, 1)
                c2 = min(c + k ,n)
                sum = arr[r2][c2] - arr[r2][c1-1] - arr[r1-1][c2] + arr[r1-1][c1-1]
                ans[r-1][c-1] = sum
        return ans