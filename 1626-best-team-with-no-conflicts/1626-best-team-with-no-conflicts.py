class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        cache = [[-1] * 1000 for  _ in range(1000)]
        def dp(i, prev):
            if i == n :
                return 0
            if cache[i][prev] != -1:
                return cache[i][prev]
            res = -1
            if prev == -1 or pairs[i][1] >= pairs[prev][1]:
                res = max(res, pairs[i][1] +  dp(i+1, i))
            res = max(dp(i+1, prev), res)
            cache[i][prev] = res
            return res
        pairs = sorted([(v, scores[i]) for i, v in enumerate(ages)])
        n = len(scores)
        return dp(0,-1)