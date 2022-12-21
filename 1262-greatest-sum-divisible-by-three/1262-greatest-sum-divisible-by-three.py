class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        dp = [0,0,0]
        for n in nums:
            for m in dp[:]:
                dp[(n+m) % 3] = max(dp[(n+m)%3] , n + m)
        return dp[0]