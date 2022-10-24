class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        stops = defaultdict(set)
        
        for r , currStops in enumerate(routes):
            for s in currStops:
                stops[s].add(r)
            
        stopSeen = set()
        routesSeen = set()
        queue = deque()
        queue.append(source)
        stopSeen.add(source)
        
        ans = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return ans
                for r in stops[curr]:
                    if r not in routesSeen : 
                        for s in routes[r]:
                            if  s not in stopSeen:
                                queue.append(s)
                                stopSeen.add(s)

                        routesSeen.add(r)
            ans += 1
        return -1