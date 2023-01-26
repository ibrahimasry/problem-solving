class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v, cost in flights:
            graph[u].append((v,cost))
        dist = [inf] * n
        dist[src] = 0
        pq = [(0,0,src)]
        while pq:
            d ,stops, node = heappop(pq)
            if node == dst:
                return d

            if stops > dist[node] or stops == k+1:
                continue
            dist[node] = stops
            for nei , cost in graph[node]:
                heappush(pq,(cost + d, stops + 1 , nei))

        return -1 