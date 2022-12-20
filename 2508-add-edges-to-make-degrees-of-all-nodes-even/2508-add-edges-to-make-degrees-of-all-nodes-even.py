class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        def f(a,b):
            return a not in graph[b] 
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        odd = [u for u in graph if len(graph[u]) % 2]
        if len(odd) > 4:
            return False
        if len(odd) == 2:
            a, b = odd
            return any(f(a,i) and f(b,i) for i in range(1,n+1))
        
        if len(odd) == 4:
            a,b,c,d=odd
            return (f(a,b) and f(c,d)) or (f(a,d) and f(b,c)) or (f(a,c) and f(b,d))
        return len(odd) == 0