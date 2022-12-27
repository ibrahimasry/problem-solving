class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        
        @cache
        def dp(i,j):
            if j - i <= 1:
                return 0
            
            ans = inf
            for k in range(i+1,j):
                ans = min(ans ,values[i] * values[k] * values[j] + dp(i,k) + dp(k,j))
            return ans
        return dp(0,len(values) - 1)