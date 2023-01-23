class Solution:
    def captureForts(self, forts: List[int]) -> int:
        res   = 0
        prev1 = -1
        for i,v in enumerate(forts):
            if  abs(v) == 1:
                if prev1 >= 0 and forts[i] == -forts[prev1]:
                    res = max(res, i - prev1 -1)
                prev1 = i
            
        return res