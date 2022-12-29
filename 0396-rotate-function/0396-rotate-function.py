class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        
        res = 0
        for i, num in enumerate(nums):
            res += (i * num)
        prev = res
        for i  in range(len(nums)-1,0,-1):
            num = nums[i]
            curr = prev - (num * (len(nums) -1))
            curr += (total - num)
            prev = curr
            res = max(res,curr)
        return res