class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ans = set()
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            ans.add((min(u,v), max(u,v)))
            
        labels = [-1] * n
        def dfs(node, parent, label):
            if labels[node] != -1:
                return labels[node]
            labels[node] = label + 1
            minLabel = label + 1
            for next in graph[node]:
                if next == parent:
                    continue

                recursiveVal = dfs(next, node, labels[node])
                if labels[node] >= recursiveVal:
                    ans.remove((min(node,next), max(node, next)))
                minLabel = min(minLabel, recursiveVal)    
            return minLabel
        dfs(0, -1, 0)
        return [[u,v] for u,v in ans]