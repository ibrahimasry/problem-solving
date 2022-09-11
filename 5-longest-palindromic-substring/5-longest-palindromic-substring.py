class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = "@#" +  "#".join(s) + "#$"
        r = 0
        c = 0
        dp = [0] * len(m)
        start = -1
        end = -1
        for i in range(1, len(m) - 1) :
            mirror = c * 2 - i
            if i < r :
                dp[i] = min(dp[mirror], r - i)
            while  m[i +  dp[i]  + 1] == m[i - dp[i] - 1]:
                dp[i] += 1
            if dp[i] * 2 > (end - start)  + 1 or end + start == -2:
                start = i - dp[i] 
                end = i + dp[i] 
                
                
            if i + dp[i] > r :
                c = i
                r = i + dp[i]
        return "".join(list(filter(lambda x: x not in ["@", "#", "$"] ,    m[start:end+1])))   
