class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        k = len(t) - 1
        dp = [-1] * m
        for i in range(n-1,-1,-1):
            if k>=0 and s[i] == t[k]:
                dp[k] = i
                k -= 1

        res = k + 1
        j = 0
        for i in range(n):
            if j < m  and s[i] == t[j]:
                while k < m and i >= dp[k]:
                    k += 1
                j+=1
                if res == 0:
                    break
                res = min(res, k-j)
        return res
