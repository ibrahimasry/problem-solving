class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
        def dp(i, j, kk):
            if (i, j ,kk) in memo:
                return memo[(i, j ,kk)]
            if pre[i][j] == 0:
                return 0
            if kk == 0:
                return 1

            ans = 0
            
            for ni in range(i+1, m):
                if pre[i][j] - pre[ni][j] > 0:
                    ans +=  dp(ni, j, kk-1)
            for nj in range(j+1, n):
                if pre[i][j] - pre[i][nj] > 0:
                    ans +=  dp(i, nj, kk-1)
            memo[(i, j, kk)] = ans
            return ans
        m = len(pizza)
        n = len(pizza[0])
        memo = defaultdict(int)
        pre = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1,-1):
                pre[i][j] = pre[i+1][j] + pre[i][j+1] - pre[i+1][j+1] + (1 if pizza[i][j] == "A" else 0)
        return dp(0,0,k-1) % (10 ** 9 + 7)

        