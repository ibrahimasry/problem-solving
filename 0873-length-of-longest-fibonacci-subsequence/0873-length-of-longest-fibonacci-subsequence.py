class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = [defaultdict(lambda :2) for _ in arr]
        index = {x: i for i, x in enumerate(arr)}

        res = 0
        for i in range(len(arr)):
            for j in range(i):
                diff = arr[i] - arr[j]
                if diff in index and index[diff] < j:
                    dp[i][arr[j]] = max(dp[i][arr[j]] , dp[j][diff] + 1)
                    res = max(res,dp[i][arr[j]])
        return res if res >= 3 else 0