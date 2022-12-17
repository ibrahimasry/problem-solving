class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        count = 0

        @cache
        def dp(i,j , maxMove):
            nonlocal count
            if maxMove < 0:
                return 0
            if not (0 <= j < n) or not (0<=i< m):
                return 1



            return sum([dp(i-1,j, maxMove-1)
            ,dp(i+1,j, maxMove-1)
            ,dp(i,j+1, maxMove-1)
            ,dp(i,j-1, maxMove-1)])
        return  dp(startRow, startColumn, maxMove) % (10**9 +7)
          