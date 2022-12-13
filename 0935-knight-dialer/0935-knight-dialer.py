class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        
        
        for i in range(1,n):
            old = dp.copy()
            dp[1] = old[6] + old[8]
            dp[2] = old[9] + old[7]
            dp[3] = old[4] + old[8]
            dp[4] = old[3] + old[9] + old[0]
            dp[5] = 0
            dp[6] = old[1] + old[7] + old[0]
            
            dp[7] = old[6] + old[2]
            dp[8] = old[3] + old[1]
            dp[9] = old[2] + old[4]
            dp[0] =  old[6] + old[4]
        return sum(dp) % (10 ** 9 +7)