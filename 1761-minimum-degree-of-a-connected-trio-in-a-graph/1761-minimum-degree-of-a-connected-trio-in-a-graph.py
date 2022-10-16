class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        degree = [0] * (n + 1)
        for u, v in edges:
            graph[min(u, v)].add(max(u, v))
            degree[u] += 1
            degree[v] += 1
        ans = sys.maxsize
        
        for n1 in range(0, n-1):
            for n2 in graph[n1]:
                for n3 in graph[n1]:
                    if n2 in graph[n3]:
                        ans = min(ans, degree[n1] + degree[n2] + degree[n3] - 6)
        return ans if ans < sys.maxsize else -1
        