class Solution:
    def racecar(self, target: int) -> int:
        
        dp = [sys.maxsize] * (target + 1)
        
        
        for t in range(target+1):
            k = t.bit_length()
            if t == 2 ** k - 1 :
                dp[t] = k
                continue
            dp[t] = min(dp[t] , k + 1 + dp[2**k -1 - t])
            
            for j in range(k-1):
                distance = t - 2 ** (k-1) + 2**j
                dp[t] = min(dp[t] , k + 1 + j  + dp[distance])
        return dp[target]