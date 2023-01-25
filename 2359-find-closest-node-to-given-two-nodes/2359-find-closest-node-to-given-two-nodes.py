class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = defaultdict(list)
        for u,v in enumerate(edges):
            if v == -1:
                continue
            graph[u].append(v)
        def bfs(node):
            q = [node]
            dist = [inf] * len(edges)
            dist[node] = 0
            for curr in q:
                for nei in graph[curr]:
                    if dist[curr] + 1 < dist[nei]:
                        q.append(nei)
                        dist[nei] = dist[curr] + 1
            return dist
        found = -1
        curr = inf
        for i , (d1,d2) in enumerate(zip(bfs(node1),bfs(node2))):
            if max(d1,d2) < curr:
                curr = max(d1,d2)   
                found = i
        return found