class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = {c:1 for c in p}
        l = 1
        for c1 , c2 in zip(p[:],p[1:]):
            v1 = ord(c1) - ord('a') + 1 
            v1 %= 26
            v2 = ord(c2) - ord('a')
            if v1 == v2:
                l += 1
            else:
                l = 1
            dp[c2] = max(dp[c2] , l)
                
        return sum(dp.values())