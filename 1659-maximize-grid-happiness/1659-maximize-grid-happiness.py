class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        
        
        
        
        def getNeighbours(j,i,  typ, curr):
            left = curr[j-1] if j > 0 else ""
            up = curr[j] if i > 0 else ""
            upDiff = 0
            leftDiff = 0
            if up == "i":
                upDiff = -30
            if up == "e":
                upDiff = 20
            if left == "i":
                leftDiff = -30
            if left == "e":
                leftDiff = 20
            nei = (1 if left != "" else 0) + (1 if up != "" else 0)
            if typ == "e":
                return 40 + (nei * 20) + upDiff + leftDiff
            return 120 - (nei * 30) + upDiff + leftDiff
        @lru_cache(None)
        def dp(pos, ext, intro, curr):
            if pos == n * m  or ext == intro == 0:
                return 0
            j = pos % n
            i = pos // n
            curr = list(curr)
            oldVal = curr[j]
            curr[j] = ""
            ans = 0
            ans = max(ans, dp(pos + 1, ext, intro, tuple(curr)))
            curr[j] = oldVal
            if ext > 0 :

                happiness = getNeighbours(j,i,  "e", curr)
                curr[j] = "e"
                ans = max(ans, happiness + dp(pos +1, ext -1, intro, tuple(curr)))
                curr[j] = oldVal
            if intro > 0:
                happiness = getNeighbours(j, i, "i", curr)
                curr[j] = "i"
                ans = max(ans, happiness + dp(pos +1, ext, intro-1, tuple(curr)))
                curr[j] = oldVal
            return ans
        
        return dp(0,  extrovertsCount, introvertsCount, tuple([''] * n))