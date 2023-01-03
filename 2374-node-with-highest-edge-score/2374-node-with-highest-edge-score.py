class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        ind = [0] * len(edges)
        
        count = 0
        node = 0
        for u, v in enumerate(edges):
            ind[v] += u
        for i , c in enumerate(ind):
            if c > count:
                count = c
                node = i
        return node