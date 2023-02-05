class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def good(target):
            take = 0
            prev = -1
            for num in nums:
                if prev > 0:
                    prev = -1
                elif num <= target:
                    take += 1
                    prev = 1
            return take >= k
        l = 1
        r = max(nums)
        while l < r:
            m = (l+r) >> 1
            if good(m):
                r = m
            else:
                l = m+1
        return l