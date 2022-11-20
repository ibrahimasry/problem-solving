class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        
        
        n = len(dist)
        eps = 1e-9
        
        dp = [[sys.maxsize] * (n+1) for _ in range(n+1)]
        
        
        for i in range(n+1):
            dp[0][i] = 0
        for i in range(1,n+1):
            dp[i][0] = ceil(dp[i-1][0] - eps) + dist[i-1]/speed
        for i in range(n+1):
            for j in range(1,i):
                dp[i][j] = dist[i-1]/speed + min(ceil(dp[i-1][j] - eps), dp[i-1][j-1])
        for i in range(n+1):
            if dp[-1][i] <= hoursBefore:
                return i
        return -1