class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], l: int, m: int) -> int:
        
        def overlap(nums, l, m):
            prev = bestPrev = sum(nums[:l])
            running = sum(nums[:l+m]) - prev
            res = prev + running
            for i in range(l+m,len(nums)):
                prev = prev - nums[i-l-m] + nums[i-m]
                bestPrev = max(bestPrev, prev)
                running = running - nums[i-m] + nums[i]
                res = max(res, bestPrev + running)
            return res
        return max(overlap(nums,l,m) , overlap(nums,m,l))
        