class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        running = nums[0]
        j = 0
        res = 1
        for i in range(1,len(nums)):
            while (running & nums[i]) > 0:
                running ^= nums[j]
                j += 1
            running |= nums[i]
            res = max(res, i - j + 1)
        return res