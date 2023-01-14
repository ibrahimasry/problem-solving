class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        graph = [defaultdict(list) for _ in range(2)]
        ans = [[inf] * n for _ in range(2)]
        for color in range(2):
            for u,v in redEdges if color == 1 else blueEdges:
                graph[color][u].append(v)
        def dfs(curr , color , l ):
            ans[color][curr] = min(ans[color][curr] , l)
            for nei in graph[color][curr]:
                if ans[color ^ 1][nei] > l + 1:
                    dfs(nei, color ^ 1, l+1)
        for color in range(2):
            for x in graph[color][0]:
                dfs(x, color ^ 1 , 1)
        res = [0]
        for c1,c2 in list(zip(*ans))[1:]:
            res.append(min(c1,c2))
            if res[-1] == inf:
                res[-1] = -1
        return res
            