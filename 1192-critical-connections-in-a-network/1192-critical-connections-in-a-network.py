class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        ans = []
        labels = [-1] * n
        curr = [-1] * n
        def dfs(node, parent, label):
            if labels[node] != -1:
                return labels[node]
            labels[node] = label + 1
            curr[node] = label + 1
            
            for next in graph[node]:
                if next == parent:
                    continue
                if labels[next] == -1 :
                    labels[node] = min(labels[node], dfs(next, node, label+1))
                    if curr[node] < labels[next]:
                        ans.append([node, next])
                else:
                    labels[node] = min(labels[node], labels[next])
            return labels[node]        
        dfs(0, -1, 0)
        return ans