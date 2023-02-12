class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        res = 0
        i = 0
        while i < len(nums):
                r = bisect.bisect(nums,upper - nums[i] ,i+1)
                l = bisect.bisect_left(nums,lower-nums[i],i+1)
                res +=  (r-l)
                i += 1


        return res