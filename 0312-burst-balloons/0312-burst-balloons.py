class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @cache
        def dp(l, r):
            
            res = 0
            
            for i in range(l, r+1):
                curr = nums[i] * nums[l-1] * nums[r+1]
                
                res = max(res, curr + dp(l,i-1) + dp(i+1,r))
            return res
        return dp(1,len(nums)-2)