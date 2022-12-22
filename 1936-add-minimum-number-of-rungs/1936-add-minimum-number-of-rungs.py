class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        
        rungs = [0] + rungs
        res = 0
        for x,y in zip(rungs,rungs[1:]):
            res += ((y-x-1)//dist)
        return res