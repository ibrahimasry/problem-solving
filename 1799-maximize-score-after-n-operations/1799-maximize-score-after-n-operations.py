class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        def gcd(x, y):
            while y :
                x , y = y, x%y
            return x
        
        @lru_cache(None)
        def dp(steps, mask):
            if mask == (1 << n -1):
                return 0
            ans = 0
            for i in range(n):
                if mask >> i & 1 == 0:
                    for j in range(i+1, n):
                        if i != j and mask >> j & 1 == 0:
                            ans = max(ans, steps * gcd(nums[i], nums[j]) + dp(steps+1, mask | 1 << i | 1 << j))
            return ans
        n = len(nums)
        return dp(1,0)