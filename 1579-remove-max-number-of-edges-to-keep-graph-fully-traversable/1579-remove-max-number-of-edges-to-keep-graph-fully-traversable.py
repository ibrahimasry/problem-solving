class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        
        
        
        class Dsu:
            def __init__(self, n):
                self.n = n
                self.parent = list(range(n))
                self.edges = 0
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            def union(self, x, y):
                r1 = self.find(x)
                r2 = self.find(y)
                if r1 != r2:
                    self.edges += 1
                    self.parent[r1] = r2
                    return 0
                return 1
        
        
        alice = Dsu(n+1)
        bob = Dsu(n+1)
        
        ans = 0
        for t, u, v in edges:
            if t == 3:
                ans += alice.union(u, v)
                bob.union(u, v)
        for t, u, v in edges:
            if t == 1:
                ans += alice.union(u, v)
            if t == 2:
                ans += bob.union(u, v)
        return ans if bob.edges == alice.edges == n - 1 else -1