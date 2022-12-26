class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        n = len(arr)
            
        dp = defaultdict(int)
        for i in range(n):
            curr = arr[i]
            if curr - diff in dp:
                dp[curr] = dp[curr-diff] + 1
            elif curr not in dp:
                dp[curr] = 1
                
        return max(dp.values())