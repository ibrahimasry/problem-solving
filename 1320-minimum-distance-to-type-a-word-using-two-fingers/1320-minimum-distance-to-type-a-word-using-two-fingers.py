class Solution:
    def minimumDistance(self, word: str) -> int:
        def getDist(x, y):
            if x == -1: return 0
            r1, c1 = divmod(x, 6)
            r2, c2 = divmod(y, 6)
            return abs(r2-r1) + abs(c2-c1)
        @lru_cache(None)
        def dp(k , i, j):
            if k == len(word) :
                return 0
            
            currIndex = ord(word[k]) - ord("A")
            ans = getDist(i, currIndex) + dp(k+1, currIndex, j)
            ans = min(ans, getDist(j, currIndex) + dp(k+1, i, currIndex))
            return ans
        return dp(0, -1, -1)