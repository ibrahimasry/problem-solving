class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        dp = [0] * (n+1)
        dp[1] = 1
        share = 0
        for i in range(2,len(dp)):
            share =  (share - dp[max(i-forget,0)] + (dp[max(i-delay,0)])) + (10 ** 9 + 7) 
            dp[i] = share % (10 ** 9 + 7)
        return sum(dp[-forget:]) % (10 ** 9 + 7)