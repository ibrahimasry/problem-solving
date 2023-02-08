class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        nextWindow  = -1
        currWindow = -1
        for i, j in enumerate(nums[:-1]):
            nextWindow = max(nextWindow,i+j)
            if i >= currWindow:
                currWindow = nextWindow
                res += 1

        return res
        