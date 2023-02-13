class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        seen = set([firstPerson, 0])
        t = inf
        pq = []
        adj = defaultdict(list)
        for u,v,t2 in meetings:
            adj[u].append((v,t2))
            adj[v].append((u,t2))
            t = min(t2,t)
        heappush(pq,(t,firstPerson))
        heappush(pq,(0,0))

        t = 0
        dist = [inf] * n
        while pq:
            t1, p1 = heappop(pq)
            if dist[p1] < t1: continue
            for (p2,t2) in adj[p1]:
                if dist[p2] > t2 and t2 >= t1:
                    heappush(pq,(t2, p2))
                    dist[p2] = t2
                    seen.add(p2)
            t = t1
        return seen
                    