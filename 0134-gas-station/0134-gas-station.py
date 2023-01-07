class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = 0
        curr = 0
        n  = len(gas)
        for i in range(n*2):
            
            c = cost[i%n]
            g = gas[i%n]
            curr = (curr - c) + g
            if curr <  0:
                res = i+1
                curr = 0
            elif  i - res == n-1:
                return res
        return -1 