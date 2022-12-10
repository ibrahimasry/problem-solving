class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        if len(set(s)) == 1 and len(s) >= 3 :
            return True
            
        dp = [[False] * (n) for i in s]

        for i in range(n-1,-1,-1):

            for j in range(i,n):
                if i == j :
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = s[i] == s[j]
                else:
                    
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
        for i in range(1,n):
            for j in range(i , n-1):
                if dp[0][i-1] and dp[i][j] and dp[j+1][-1]:
                    return True
        return False