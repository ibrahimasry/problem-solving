class Solution:
    def earliestAndLatest(self, n, F, S):
        ans = set()
        lru_cache(None)
        def dfs(pos):
            M, pairs = len(pos), []
            if M < 2: return

            for j in range(M//2):
                a, b = pos[j], pos[-1-j]
                if (a, b) == (F, S):
                    return [1,1]
                if a != F and b != F and a != S and b != S:
                    pairs.append((a, b))
            addon = (F, S) if M%2 == 0 else tuple(set([F, S, pos[M//2]]))
            minx =  sys.maxsize
            maxx = -sys.maxsize
            for elem in product(*pairs):
                result =  dfs(sorted(elem + addon))
                minx = min(result[0], minx)
                maxx = max(result[1], maxx)
            return [minx + 1, maxx + 1]    


        return dfs(tuple(range(1, n+1)))
        