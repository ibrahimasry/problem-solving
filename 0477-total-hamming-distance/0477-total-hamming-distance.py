class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        zeros = [0] * 32
        ones = [0] * 32
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(0,32):
                if (curr >> j) & 1 != 1:
                    zeros[j] += 1
                else :
                    ones[j] += 1
        for num in nums:
            for j in range(0,32):
                if (num >> j) & 1:
                    if num >> j:
                        res += zeros[j]
                    else :
                        res += ones[j]
        return res                              