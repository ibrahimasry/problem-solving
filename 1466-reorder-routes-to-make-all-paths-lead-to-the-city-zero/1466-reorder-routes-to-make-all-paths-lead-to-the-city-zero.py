class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connections = set(tuple(curr) for curr in connections)
        
        
        graph = defaultdict(list)
        
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        res = 0
        
        def dfs(node, parent):
            nonlocal res
            for nei in graph[node]:
                if nei == parent:
                    continue
                if (node,nei) in connections:
                    res += 1
                dfs(nei,node)
        dfs(0,-1)
        return res