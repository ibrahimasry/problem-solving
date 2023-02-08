class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 0
        
        mxW  = -1
        curr = -1
        dist = len(nums) - 1
        for i, j in enumerate(nums):
            mxW = max(mxW,i+j)

            if i >= curr:
                curr = mxW
                res += 1
            if curr >= dist:
                return res

        return res
        