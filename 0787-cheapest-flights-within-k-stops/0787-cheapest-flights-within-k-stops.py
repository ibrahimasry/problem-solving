class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [inf] * n
        prev = [inf] * n
        prev[src] = 0
        
        for _ in range(k+1):
            for u , v , cost in flights:
                if prev[u] + cost < dist[v]:
                    dist[v] = prev[u] + cost
            prev = dist
            prev[src] = 0
            dist = [inf] * n
        return -1 if prev[dst] == inf else prev[dst]