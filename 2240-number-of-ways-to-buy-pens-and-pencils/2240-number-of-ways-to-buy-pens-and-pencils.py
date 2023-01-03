class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0
        
        for c in range(total//cost1 + 1):
            res += (((total-c * cost1)//cost2) + 1)
        return res