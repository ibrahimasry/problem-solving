class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        res = 0
        minn = -1
        maxn = -1
        start = -1
        
        for r in range(len(nums)):
            curr = nums[r]
            if curr < minK or curr > maxK:
                start = r
            if curr == maxK:
                maxn = r
            if curr == minK:
                minn = r
            res += max(0 , (min(minn, maxn) - start))
        return res