class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp  = [False] * (len(nums) + 1)
        
        dp[0] = True
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                dp[i+1] = dp[i-1]
            if i - 2 < 0 or dp[i+1]: 
                continue
            if nums[i] == nums[i - 1] == nums[i-2]:
                dp[i+1] = dp[i-2]

            if nums[i] == nums[i-1] + 1 == nums[i-2]+2:
                dp[i+1] = dp[i-2]
        return dp[-1]