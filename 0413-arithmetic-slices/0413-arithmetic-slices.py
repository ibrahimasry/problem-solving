class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        l = 0
        prev = nums[1] - nums[0]
        res = 0
        for i in range(2,len(nums)):
            num = nums[i]
            if num - nums[i-1] == prev:
                
                res += (l+1)
                l += 1
            else:
                l = 0
                prev = num - nums[i-1]
        return res