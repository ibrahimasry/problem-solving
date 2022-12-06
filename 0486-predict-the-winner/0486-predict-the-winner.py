class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(start, end):
            if start > end:
                return 0
            return max(nums[start] + min(dp(start + 1, end-1) , dp(start+2, end)) , 
                       nums[end] + min(dp(start+1, end -1), dp(start, end-2)))
        return sum(nums) - 2* dp(0, len(nums)-1) <= 0