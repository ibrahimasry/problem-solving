class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(coins)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
            
        steps = [30000] * n
        q = deque([])
        seen = set()
        for i , v in enumerate(indegree):
            if v == 1:
                q.append(i)
        
        while q:
            curr = q.popleft()
            steps[curr] -= 1
            if steps[curr] > 0:
                n -= 1

                for nei in graph[curr]:
                    if coins[curr] > 0:
                        steps[nei] = min([steps[curr], 2, steps[nei]])
                    elif  coins[curr] == 0:
                        steps[nei] = min([steps[curr], 30000, steps[nei]])
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)

        return max(0,(n - 1)) * 2
            