class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        
        n = len(nums)
        m = nums[n//2]
        res = 0
        
        for curr in nums:
            res += abs(curr - m)
        return res