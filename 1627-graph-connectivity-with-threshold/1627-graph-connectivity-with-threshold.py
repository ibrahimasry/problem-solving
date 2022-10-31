class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent = list(range(n+1))
        def union(x, y):
            p1 = find(x)
            p2 = find(y)
            if p1 != p2:
                parent[p1] = p2
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        
        for x in range(threshold+1, n+1):
            for y in range(x+x, n+1, x):
                union(x, y)
        return [find(x) == find(y) for x, y in queries]