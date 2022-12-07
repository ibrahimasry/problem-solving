class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        
        minDist = sys.maxsize
        res = 0
        
        dist = [sys.maxsize] * n
        
        dist[0] = 0
        count = [0] * n
        count[0] = 1
        graph = defaultdict(list)
        
        for u, v, t in roads:
            graph[u].append([v, t])
            graph[v].append([u, t])
        pq = [[0,0]]
        seen = set()
        
        while pq:
            currDist, curr = heapq.heappop(pq)
            if dist[curr] < currDist:
                continue
            for u, t in graph[curr]:
                if dist[curr] + t < dist[u] :
                    dist[u] = dist[curr] + t
                    count[u] = count[curr]
                    heapq.heappush(pq, [dist[u], u])
                elif dist[curr] + t == dist[u]  :
                    count[u] += count[curr]
        return count[n-1] % (10 ** 9 + 7)