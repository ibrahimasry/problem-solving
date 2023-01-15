class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        res = 0
        parent = list(range(len(vals)))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y ):
            nonlocal res
            r1 = find(x)
            r2 = find(y)
            if r1 != r2:
                if vals[r1] > vals[r2]:
                    parent[r2] = r1
                else:
                    parent[r1] = r2 
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        valToNode = defaultdict(list)
        for i , val in enumerate(vals):
            valToNode[val].append(i)
        
        for val in sorted(valToNode):
            for node in valToNode[val]:
                for nei in graph[node]:
                    if vals[node] >= vals[nei]:
                        union(node, nei)
            groups = defaultdict(int)
            for node in valToNode[val]:
                groups[find(node)] = groups[find(node)] + 1
            for val in groups.values():
                res += val * (val+1) // 2
        return res 