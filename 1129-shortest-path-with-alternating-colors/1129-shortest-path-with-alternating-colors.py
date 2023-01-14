class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        red = defaultdict(list)
        blue = defaultdict(list)
        ans = [[inf] * n for _ in range(2)]
        for u,v in redEdges:
            red[u].append(v)
        for u,v in blueEdges:
            blue[u].append(v)
        
        def dfs(curr , color , l ):
            ans[color][curr] = min(ans[color][curr] , l)
            graph = red[curr] if color == 0 else blue[curr]
            for nei in graph:
                if ans[color ^ 1][nei] > l + 1:
                    dfs(nei, color ^ 1, l+1)
        for x in red[0]:
            dfs(x,1 , 1)
        for x in blue[0]:
            dfs(x,0, 1)
        res = [0]
        for c1,c2 in list(zip(*ans))[1:]:
            res.append(min(c1,c2))
            if res[-1] == inf:
                res[-1] = -1
        return res
            