class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ban = set(restricted)
        seen = set()
        def dfs(node):
            seen.add(node)
            res=1
            for nei in graph[node]:
                if nei in seen or nei in ban:
                    continue
                res += dfs(nei)
            return res

        return dfs(0)