class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
            
        dp = defaultdict(int)
        for curr in arr:
            dp[curr] = dp[curr-diff] + 1
        return max(dp.values())