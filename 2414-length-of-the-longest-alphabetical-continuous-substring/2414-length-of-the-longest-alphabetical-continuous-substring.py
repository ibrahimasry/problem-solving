class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = 1
        
        l = 1
        for i in range(1,len(s)):
            c = s[i]
            c1 = s[i-1]
            if ord(c1) + 1 == ord(c):
                l += 1
            else :
                l = 1
            res = max(l, res)

        return res