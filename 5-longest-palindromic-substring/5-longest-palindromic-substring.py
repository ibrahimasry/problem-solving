class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = "@#" +  "#".join(s) + "#$"
        r = 0
        c = 0
        dp = [0] * len(m)
        rm = -1
        cm = -1
        for i in range(1, len(m) - 1) :
            mirror = c * 2 - i
            if i < r :
                dp[i] = min(dp[mirror], r - i)
            while  m[i +  dp[i]  + 1] == m[i - dp[i] - 1]:
                dp[i] += 1
                
            if i + dp[i] > r :
                c = i
                r = i + dp[i]
            if dp[i] > rm :
                rm , cm = dp[i], i
        return  s[(cm-rm)//2: (cm+rm)//2]
