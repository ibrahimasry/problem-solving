class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
        s = []
        
        res = 0
        
        for i in range(0, len(nums) + 1):
            while s and (i == len(nums) or  nums[s[-1]] >= nums[i] ):

                curr = nums[s.pop()]
                left = (0 if len(s) == 0 else s[-1]+1)
                total = prefix[i] - prefix[left]
                res = max(res, total * curr)
            s.append(i)
        return res % (10 ** 9 + 7)