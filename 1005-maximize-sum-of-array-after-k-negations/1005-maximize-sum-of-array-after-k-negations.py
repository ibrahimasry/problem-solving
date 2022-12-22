class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k and i < len(nums) and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1
        return sum(nums) - (k % 2) * 2 * min(nums)
        
        
        