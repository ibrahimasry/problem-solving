class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        indegrees = [0] * n
        for u,v in edges:
            indegrees[v] += 1
            graph[u].append(v)
        ans = [set() for _ in range(n)]
        
        
        q = deque()
        for v , d in enumerate(indegrees):
            if d == 0:
                q.append(v)
        while q:
            curr = q.popleft()
            
            for nei in graph[curr]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
                ans[nei] |= {curr} | ans[curr]
        ans = [sorted(list(curr)) for curr in ans]
        return ans