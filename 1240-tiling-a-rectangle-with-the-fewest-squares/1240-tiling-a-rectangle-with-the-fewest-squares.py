class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        
        @cache
        def dp(sky):
            start = -1
            minH = inf
            for i, h in enumerate(sky):
                if h < minH:
                    minH = h
                    start = i
            if minH == n:
                return 0
            res = sys.maxsize
            sky = list(sky)
            for end in range(start, m):
                if sky[end] != minH:
                    break
                sides = end - start + 1
                if minH + sides > n:
                    break

                sky[start:end+1] = [minH + sides] * sides
                res = min(dp(tuple(sky)) + 1 , res)
            return res
                
        
        return dp(tuple([0] * (m)))