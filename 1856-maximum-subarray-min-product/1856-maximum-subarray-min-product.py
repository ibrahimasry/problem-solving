class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
        s = [-1]
        res = 0
        for i in range(0, len(nums) + 1):
            while len(s) > 1 and (i == len(nums) or  nums[s[-1]] >= nums[i] ):
                res = max(res, nums[s.pop()] * (prefix[i] - prefix[s[-1] + 1]))
            s.append(i)
        return res % (10 ** 9 + 7)