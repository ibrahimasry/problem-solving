class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        ans = 0
        dp = [0] * (high + 1 )
        dp[0] = 1
        for l in range(high + 1):
            if l - zero >= 0:
                dp[l] += dp[l-zero]
            if l - one >= 0 :
                dp[l] += dp[l-one]
        
        return sum(dp[low:]) % (10**9 +7)