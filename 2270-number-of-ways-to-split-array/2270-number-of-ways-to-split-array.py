class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        overall = sum(nums)
        res = 0
        running = 0
        for n in nums:
            
            running += n 
            if overall - running  <= running:
                res += 1
        return res-1 if overall >= 0 else res