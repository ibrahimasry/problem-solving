class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return "/".join(nums)
        if len(nums) > 1:
            return nums[0] + "/" + "(" + "/".join(nums[1:]) + ")"