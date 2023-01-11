class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        c = 0
        res = 0
        for i in nums:
            if i:
                c += 1
            else:
                c = 0
            res = max(c,res)
        return res