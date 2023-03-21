class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        
        curr = 0
        
        for n in nums:
            if n == 0:
                curr += 1
                res += curr
            else :
                curr = 0
        return res