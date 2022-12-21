class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = sum([a for a, b in costs])
        diff = sorted([a-b for a, b in costs])
        n = len(costs)//2
        for d in range(n, 2*n):
            res -= diff[d]
        return res