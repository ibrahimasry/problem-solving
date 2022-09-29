class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        ans = []
        lows = [-1] * n
        ids = [-1] * n
        def dfs(node, parent, label):
            if lows[node] != -1:
                return lows[node]
            lows[node] = ids[node] = label + 1
            
            for next in graph[node]:
                if next == parent:
                    continue
                lows[node] = min(lows[node], dfs(next, node, label+1))
                if ids[node] < lows[next]:
                    ans.append([node, next])
            return lows[node]        
        dfs(0, -1, 0)
        return ans