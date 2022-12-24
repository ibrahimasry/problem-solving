class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[0] * 3 for _ in range(2)]
        
        dp[0][0] = 1
        
        for d in range(1, n+1):
            curr = [[0] * 3 for _ in range(2)]
            for i in range(2):
                for j in range(3):
                    curr[i][0] += dp[i][j]
                    curr[i][0] %=  (10**9 + 7)
            for i in range(3):
                curr[1][0] += dp[0][i]
                curr[1][0] %=  (10**9 + 7)
            for i in range(2):
                for j in range(1,3):
                    curr[i][j] += dp[i][j-1]
                    curr[i][j] %=  (10**9 + 7)
            dp = curr
        return sum([sum(arr) for arr in dp]) % (10**9 + 7)