class Solution:
    def earliestAndLatest(self, n, F, S):
        ans = set()
        lru_cache(None)
        def dfs(pos, i):
            M, pairs = len(pos), []
            if M < 2: return

            for j in range(M//2):
                a, b = pos[j], pos[-1-j]
                if (a, b) == (F, S):
                    ans.add(i)
                    return
                if a != F and b != F and a != S and b != S:
                    pairs.append((a, b))
            addon = (F, S) if M%2 == 0 else tuple(set([F, S, pos[M//2]]))
            for elem in product(*pairs):
                dfs(sorted(elem + addon), i + 1)

        dfs(list(range(1, n+1)), 1)
        return [min(ans), max(ans)]
        