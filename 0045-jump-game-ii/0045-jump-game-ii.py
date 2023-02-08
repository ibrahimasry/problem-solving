class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        mxW  = -1
        curr = -1
        for i, j in enumerate(nums[:-1]):
            mxW = max(mxW,i+j)

            if i >= curr:
                curr = mxW
                res += 1

        return res
        