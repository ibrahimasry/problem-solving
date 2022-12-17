class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        
        for u, v in roads:
            degrees[u] += 1
            degrees[v] += 1
        res = 0
        for i, x in enumerate(sorted(degrees),1):
            res += x * (i)
        return res