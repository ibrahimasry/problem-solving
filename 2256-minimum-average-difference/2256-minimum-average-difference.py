class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        overall = sum(nums)
        minDiff = sys.maxsize

        n = len(nums)
        curr = 0
        res = -1
        for i in range(len(nums)):
            curr += nums[i]
            l = curr  // (i+1)
            r = 0
            if i != n -1:
                val = overall - curr
                r =  val  // (n-i-1)
            currDiff = abs(l-r)
            if currDiff < minDiff:
                res = i
                minDiff = currDiff
        return res