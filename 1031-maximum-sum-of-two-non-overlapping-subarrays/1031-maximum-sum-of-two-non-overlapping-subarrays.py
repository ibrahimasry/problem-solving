class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], l: int, m: int) -> int:
        
        def overlap(nums, l, m):
            f = best = sum(nums[:l])
            s = sum(nums[:l+m]) - f
            res = f + s
            for i in range(l+m,len(nums)):

                best = max(best,f - nums[i-l-m] + nums[i-m])
                s = s - nums[i-m] + nums[i]
                f = f - nums[i-l-m] + nums[i-m]
                res = max(res, best + s)
            return res
        return max(overlap(nums,l,m) , overlap(nums,m,l))
        