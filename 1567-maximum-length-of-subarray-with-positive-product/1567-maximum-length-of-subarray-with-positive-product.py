class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        res = 0
        
        n = len(nums)
        curr = 1
        start = 0
        for i in range(n):
            num = nums[i]
            curr *= num
            if curr > 0:
                res = max(i - start + 1, res)
            if curr == 0:
                curr = 1
                start = i + 1
        start = n-1
        curr = 1
        for i in range(n-1, -1, -1):
            curr *= nums[i]
            if curr > 0:
                res = max(start - i + 1, res)
            if curr == 0:
                start = i -1
                curr = 1
        return res