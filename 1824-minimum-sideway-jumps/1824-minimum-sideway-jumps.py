class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1,0,1]
        for  b in obstacles:
            if b:
                dp[b-1] = inf
            for i in range(3):
                if i+1 == b:
                    continue
                dp[i] = min(dp[i] , min(dp[(i+1)%3] + 1, dp[(i+2)% 3] + 1))
        return min(dp)