class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = defaultdict(list)
        for u,v in enumerate(edges):
            if v == -1:
                continue
            graph[u].append(v)
        def bfs(node):
            q = deque([node])
            dist = [inf] * len(edges)
            dist[node] = 0
            while q:
                curr = q.popleft()
                for nei in graph[curr]:
                    if dist[curr] + 1 < dist[nei]:
                        q.append(nei)
                        dist[nei] = dist[curr] + 1
            return dist
        dist1 = bfs(node1)
        dist2 = bfs(node2)
        found = -1
        curr = inf
        for i , (d1,d2) in enumerate(zip(dist1,dist2)):
            if max(d1,d2) < curr:
                curr = max(d1,d2)   
                found = i
        return found