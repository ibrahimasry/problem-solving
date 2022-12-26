class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(lambda:1) for _ in range(n)]
        res = 1
        for i in range(n):
            for j in range(i):
                dp[i][nums[i] - nums[j]] = dp[j][nums[i]-nums[j]] + 1
                res = max(res,dp[i][nums[i] - nums[j]])
        return res