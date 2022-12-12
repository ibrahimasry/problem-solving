class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
    
        if n > m:
            return self.shortestCommonSupersequence(str2, str1)
        dp = [[""] * (m +1)for _ in range(n+1)]
        
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                else :
                    dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1] 
        
        res, i, j = "", 0, 0
        for c in dp[-1][-1]:
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i, j = i + 1, j + 1
        return res + str1[i:] + str2[j:]

