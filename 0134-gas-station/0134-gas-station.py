class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        res = 0
        curr = 0
        
        for i, (c,g) in enumerate(zip(cost,gas)):
            curr = (curr - c) + g
            if curr <  0:
                res = i+1
                curr = 0
        return res % len(gas)