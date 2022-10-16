class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        
        lru_cache(None)
        def dp(k, i):
            if k == 0 and i == n :
                return 0
            if k == 0 or i == n :
                return sys.maxsize
            ans = sys.maxsize
            for j in range(i, n):
                ans = min(ans, dist[i][j] + dp(k-1, j+1))
            return ans
        dist = [[0] * len(houses) for _ in houses]
        
        
        n = len(houses)
        houses.sort()
        for i in range(n):
            for j in range(i, n):
                mid = houses[(i + j) // 2]
                for h in range(i, j+1):
                    dist[i][j] += abs(mid - houses[h])
        dp = [[sys.maxsize] * k for _ in houses]
        for i in range(n):
            dp[i][0] = dist[0][i]
        for kk in range(1, k):
            for i in range(0, n):
                for j in range(i):
                    dp[i][kk] = min(dp[i][kk] , dp[j][kk-1] + dist[j+1][i])
        return dp[-1][-1]