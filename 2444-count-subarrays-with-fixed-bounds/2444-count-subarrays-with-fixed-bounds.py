class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        res = 0
        minn = -1
        maxn = -1
        start = 0
        lastmin = -1
        lastmax = -1
        
        for r in range(len(nums)):
            curr = nums[r]
            if curr < minK or curr > maxK:
                start = r+1
                minn = -1
                maxn = -1
                lastmin = -1
                lastmax = -1

                continue
            if curr == maxK:
                if maxn == -1:
                    maxn = r
                elif maxn <= minn or minn == -1:
                    maxn = r
                    minn = lastmin
                lastmax = r
            if curr == minK:
                if minn == -1:
                    minn = r
                elif minn <= maxn or maxn == -1:
                    minn = r
                    maxn = lastmax
                lastmin = r
            if minn > -1 and maxn > -1:
                res += abs(start - min(minn, maxn)) + 1
        return res