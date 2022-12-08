class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        seen = set()
        
        
        def dfs(node):
            if node == destination:
                return True
            seen.add(node)
            for u in graph[node]:
                if u in seen:
                    continue
                if dfs(u):
                    return True
            return False
                
        return dfs(source)