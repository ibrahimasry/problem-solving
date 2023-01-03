class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = 1
        
        l = 1
        for c1 , c in zip(s[:] , s[1:]):
            if ord(c1) + 1 == ord(c):
                l += 1
            else :
                l = 1
            res = max(l, res)

        return res