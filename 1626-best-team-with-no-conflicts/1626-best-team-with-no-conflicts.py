class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        pairs = sorted([(v, scores[i]) for i, v in enumerate(ages)])
        n = len(scores)
        dp = [-1] * n
        for i in range(n):
            dp[i] = pairs[i][1]
            for j in range(i):
                if pairs[i][1] >= pairs[j][1]:
                    dp[i] = max(dp[i] , dp[j] + pairs[i][1])
        return max(dp)