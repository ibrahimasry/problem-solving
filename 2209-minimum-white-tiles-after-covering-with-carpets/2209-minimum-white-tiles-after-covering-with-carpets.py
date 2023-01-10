class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        @cache
        def dp(i, k):
            if i >= n:
                return 0
            if k == 0:
                return prefix[n] - prefix[i]
            return min(dp(i+carpetLen, k-1) ,int(floor[i]) + dp(i+1,k))
        prefix = [0] + list(accumulate(map(int,floor[:])))
        n = len(floor)
        return dp(0,numCarpets)