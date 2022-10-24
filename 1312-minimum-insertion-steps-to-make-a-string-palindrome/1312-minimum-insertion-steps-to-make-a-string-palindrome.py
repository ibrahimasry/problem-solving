class Solution:
    def minInsertions(self, s: str) -> int:
        
        
        n = len(s)
        dp = [[0] * (n) for _ in range(n)]
        
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i < 2:
                        dp[i][j] = j - i + 1
                    else :
                        dp[i][j] = 2 + dp[i+1][j-1]
                else :
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return n - dp[0][n-1]
        