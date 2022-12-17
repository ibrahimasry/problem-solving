class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        
        for u, v in roads:
            degrees[u] += 1
            degrees[v] += 1
        return sum([x*i for i, x in enumerate(sorted(degrees),1)])
