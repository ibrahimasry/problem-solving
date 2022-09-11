class Solution:
    def maxProduct(self, s: str) -> int:
        m = "@#" +  "#".join(s) + "#$"
        r = 0
        c = 0
        dp = [0] * len(m)
        rm = -1
        cm = -1
        for i in range(1, len(m) - 1) :
            mirror = c * 2 - i
            if i < r :
                dp[i] = min(dp[mirror], r - i)    
            while  m[i +  dp[i]  + 1] == m[i - dp[i] - 1]:
                dp[i] += 1
                
            if i + dp[i] > r :
                c = i
                r = i + dp[i]
        dp = dp[2:-2:2]
        n = len(s)
        left = [0] * n
        for i in range(n) :
            r = i + (dp[i]-1)//2
            left[r] = max(left[r], dp[i])
        for i in range(n-2, -1,-1):
            left[i] = max(left[i+1] - 2, left[i])
        for i in range(1, n):
            left[i] = max(left[i], left[i-1])
        right = [0] * n
        for i in range(n) :
            l = i - (dp[i]-1)//2
            right[l] = max(right[l] , dp[i])
        for i in range(1, n):
            right[i] = max(right[i-1] - 2, right[i])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i], right[i+1])
        res = 0
        for i in range(n-1):
            res = max(left[i] * right[i+1], res)
        return res    

        