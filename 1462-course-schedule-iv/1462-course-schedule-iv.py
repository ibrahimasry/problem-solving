class Solution:
    def checkIfPrerequisite(self, n: int, preq: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        degree = [0] * n
        for u, v in preq:
            degree[v] += 1
            graph[u].append(v)
        
        start = deque([])
        
        for i , v in enumerate(degree):
            if v == 0:
                start.append(i)
        ind = defaultdict(set)
        
        while start :
            curr = start.popleft()
            for nei in graph[curr]:
                degree[nei] -= 1
                ind[nei].add(curr)
                ind[nei] |= ind[curr]
                if degree[nei] == 0:
                    start.append(nei)
        res = []
        
        for u, v in queries:
            if u in ind[v]:
                res.append(True)
            else :
                res.append(False)
        return res