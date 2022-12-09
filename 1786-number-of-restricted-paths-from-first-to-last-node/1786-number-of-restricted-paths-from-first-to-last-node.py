class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        
        @lru_cache(None)
        def dp(curr):
            if curr == n:
                return 1
            
            ans = 0
            for nei, i in graph[curr]:
                if dist[nei] < dist[curr]:
                    ans += dp(nei)
            return ans
        
        graph = defaultdict(list)
        dist = [sys.maxsize] * (n+1)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        pq = [(0,n)]
        dist[n] = 0
        seen = set()
        
        while pq:
            minDist, node = heapq.heappop(pq)
            
            seen.add(node)
            
            for u , w2 in graph[node]:
                if u in seen:
                    continue
                if minDist + w2 < dist[u]:
                    dist[u] = minDist + w2
                    heapq.heappush(pq, (minDist +  w2, u))
        return dp(1) % (10 ** 9 + 7)