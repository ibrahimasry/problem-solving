class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums)/2 < k:
            return 0
        @cache
        def dp(i, curr):
            if i == n:
                return 1
            ans = 0
            
            if curr + nums[i] < k:
                ans += dp(i+1, curr + nums[i])
            ans += dp(i+1, curr)
            return ans
        n = len(nums)
        mod = 10**9 + 7
        return (((2 ** n)%mod - (dp(0,0)*2) % mod)  + mod) % (10 ** 9 + 7)