class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)  < n - 1:
            return -1
        
        graph = defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        seen = set()
        
        def dfs(node):
            if node in seen:
                return False
            seen.add(node)
            for nei in graph[node]:
                dfs(nei)
            return True
        return sum([dfs(i) for i in range(n)]) - 1