class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        seen = set()
        q = deque()
        n = len(graph)
        for i in range(n):
            seen.add((1 << i, i))
            q.append((1<<i,i))
            
        res = 0
        while deque:
            for _ in range(len(q)):
                m, curr = q.popleft()
                if m == (1 << n) - 1:
                    return res
                for ne in graph[curr]:
                    if (m | 1 << ne , ne) in seen:
                        continue
                    q.append((( m | 1 << ne , ne )))
                    seen.add(( m | 1 << ne , ne ))
            res += 1
        return -1