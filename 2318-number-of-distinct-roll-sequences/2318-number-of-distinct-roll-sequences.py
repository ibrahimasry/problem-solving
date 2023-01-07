class Solution:
    def distinctSequences(self, n: int) -> int:
        @cache
        def dp(c,p,pp):
            if c == 0:
                return 1
            ans = 0
            for i in range(1,7):
                if pp  and (pp == i):
                    continue
                if p and p == i:
                    continue
                if p and  gcd(p,i) != 1 :
                    continue
                
                ans += dp(c - 1, i, p) % (10**9+7)
                ans %= (10**9+7)

            return ans % (10**9+7)

        return dp(n,0,0)  % (10**9+7)
