class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        start = -1
        ind = defaultdict(int)
        for  u,v in pairs:
            graph[u].append(v)
            ind[u] += 1
            start = u
            ind[v] -= 1
        for k in ind:
            if ind[k] > 0:
                start = k
        path = []
        def dfs(start):
            while graph[start]:
                nex = graph[start].popleft()
                dfs(nex)
                path.append([start,nex])
                
        dfs(start)
        return path[::-1]
        