class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        
        def maxSlice(arr):
            m = len(arr)
            
            dp = [[0] * (n) for _ in range(m)]
            
            
            for i  in range(m):
                for j in range(n):
                    dp[i][j] = max(dp[i-1][j] if i > 0 else 0 , arr[i] + (dp[i-2][j-1] if i > 1 and j > 0 else 0))
            return dp[m-1][n-1]
        n = len(slices) // 3
        return max(maxSlice(slices[1:]), maxSlice(slices[:-1]))