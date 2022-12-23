class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        grow = sorted([[v,i] for i,v in enumerate(growTime)], reverse=True)
        
        res = 0
        currPlant = 0
        for v, i in grow:
            currPlant += plantTime[i]
            res = max(res, currPlant + v)
        return res