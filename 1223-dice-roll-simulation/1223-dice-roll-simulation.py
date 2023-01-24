class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10 ** 9 + 7
        @cache
        def dp(j,last,count):
            if j == n:
                return 1
            ans = 0
            
            for k in range(6):
                if k == last and rollMax[last] == count:
                    continue
                if last == k:
                    ans += dp(j+1,last, count +1)
                else :
                    ans += dp(j+1,k,1)
            return ans % mod
        return dp(0,-1,0)