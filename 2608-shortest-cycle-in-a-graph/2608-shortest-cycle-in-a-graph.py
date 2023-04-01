class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        res = inf
        
        
        graph =  defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
            
        for node in range(n):
            q = deque([node])
            dist = [inf] * n
            dist[node] = 0
            while q:
                curr = q.popleft()
                for nei in graph[curr]:
                    if dist[nei]  == inf:
                        
                        dist[nei] = dist[curr] + 1
                        q.append(nei)
                    elif dist[nei] >= dist[curr]:
                        res = min(res, dist[nei] + dist[curr] + 1 )
                        
        return -1 if res == inf else res