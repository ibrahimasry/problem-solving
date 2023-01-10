class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        req = [0] * n
        
        for u,v in relations:
            req[v-1] |= (1 << (u-1) )
        dp = [inf] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == inf:
                continue
            cand = []
            for i in range(n):
                if (mask & 1 << i) == 0 and (req[i] & mask) == req[i]:
                    cand.append(i)
            for choice in combinations(cand,min(k,len(cand))):
                mask2 = mask
                for c in choice:
                    mask2 |= (1 << c)
                dp[mask2] = min(dp[mask2] , dp[mask] + 1)
        return dp[-1]