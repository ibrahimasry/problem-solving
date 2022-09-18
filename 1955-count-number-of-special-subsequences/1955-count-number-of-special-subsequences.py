class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        
        
        
        dp = [0] * 3
        mod = (10 ** 9 + 7)       
        
        for n in nums:
            if n == 0:
                dp[n] = dp[n] * 2 + 1
            else :
                dp[n] = dp[n-1] + dp[n] * 2 
            dp[n] %= mod
        return dp[2]  
        