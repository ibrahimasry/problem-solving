class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        if len(set(nums)) == 1:
            return 0
        prev = nums[0]
        prevCount = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] == prev:
                prevCount += 1
 
            else :
                prev = nums[i]
                res += i 
                prevCount = 1

        return res -1