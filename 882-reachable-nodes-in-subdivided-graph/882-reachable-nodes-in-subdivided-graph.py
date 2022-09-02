class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        
        graph = defaultdict(list)
        
        for v, u , w in edges :
            graph[v].append((u, w + 1))
            graph[u].append((v, w + 1))
            
        dist =  [sys.maxsize] * n
        
        dist[0] = 0
        pq =[(0,0)]
        
        while pq :
            d , v = heappop(pq)
            for u, currDist in graph[v]:
                if(currDist + d < dist[u])  and currDist + d <= maxMoves :
                    dist[u] = currDist + d
                    heappush(pq, (dist[u] , u))
            
        ans = reduce(lambda a, b : a + 1 if b <= maxMoves else a , dist , 0)                 
        for v, u , w in edges:
            if dist[u] > maxMoves and dist[v] > maxMoves :
                continue
            cnt1 = max(maxMoves  - dist[v], 0)
            cnt2 = max(maxMoves  - dist[u] , 0)
            ans += min(cnt1+cnt2 , w)
        return ans    
            
        