class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        seen = [-1] * len(graph)
        
        def dfs(node, prev):
            if seen[node] != -1:
                return seen[node] == prev
            seen[node] = prev
            for curr in graph[node]:
                if dfs(curr, prev ^ 1) == False:
                    return False
            return True
        for i in range(len(graph)):
            if seen[i] == -1 and dfs(i, 0) == False:
                return False
        return True

        