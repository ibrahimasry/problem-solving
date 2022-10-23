class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        
        n = len(stones)
        dp = [-sys.maxsize] * n + [0,0,0]
        
        
        for i in range(n-1, -1,-1):
            for k in [1,2,3]:
                dp[i] = max(dp[i] , sum(stones[i:i+k]) - dp[i+k])
                
        res = dp[0]
        
        if res < 0:
            return "Bob"
        if res > 0 :
            return "Alice"
        return "Tie"