class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        
        def dfs(node):
            if node in seen:
                return 0
            seen.add(node)
            ans = 1
            for nei in graph[node]:
                ans += dfs(nei)
            return ans
        ans = 0
        prev = 0
        
        for i in range(n):
            comp = dfs(i)
            ans += comp * prev
            prev += comp
        return ans