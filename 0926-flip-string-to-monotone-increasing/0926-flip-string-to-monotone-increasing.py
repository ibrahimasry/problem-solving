class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        one = zero = 0
        
        res = len(s)
        
        for c in s:
            if c == "0":
                zero += 1
        res = min(zero,res)
        
        for c in s:
            if c == "1":
                one += 1
            else :
                zero -=1
            res = min(res, one + zero)
        return res