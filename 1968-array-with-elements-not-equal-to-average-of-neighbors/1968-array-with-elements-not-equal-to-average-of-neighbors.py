class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        l = 0
        r = 0
        
        while l + r < len(nums):
            if l <= r:
                res.append(nums[l])
                l += 1
            else :
                res.append(nums[len(nums) - 1 - r])
                r += 1
        return res