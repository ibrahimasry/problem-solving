class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        count = [0] * (len(edges)+1)
        seen = set(tuple(curr) for curr in guesses)
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, parent):
            
            c = 0
            for nei in graph[node]:
                if nei == parent:
                    continue
                if (node,nei) in seen:
                    c += 1
                c += dfs(nei,node)
            count[node] = c
            return c
        def dfs2(node,parent, out):
            count[node] += out
            for nei in graph[node]:
                c = 0
                if nei == parent:
                    continue
                if (node,nei) in seen:
                    c -= 1
                if (nei,node) in seen:
                    c += 1
                dfs2(nei,node, count[node] - count[nei] + c)
        dfs(0,-1)
        dfs2(0,-1,0)
        res = 0
        for c in count:
            if c >= k:
                res += 1
        return res