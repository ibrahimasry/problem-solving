class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, j, k):
            if i > j  or k == len(multipliers):
                return 0
            curr = multipliers[k]
            l = nums[i]
            r = nums[j]
            
            return max(nums[i] * multipliers[k] + dp(i+1,j, k+1) , nums[j] * multipliers[k] + dp(i,j-1, k+1))
        n = len(nums)
        return dp(0, len(nums)-1, 0)