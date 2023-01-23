class Solution:
    def captureForts(self, forts: List[int]) -> int:
        res = -1
        prev1 = None
        prev0 = None
        for i,v in enumerate(forts):
            if v == 1:
                if prev0 != None:
                    res = max(res, abs(prev0-i))
                prev0 = None
                prev1 = i
            elif v == -1:
                if prev1 != None:
                    res = max(res, abs(prev1-i))
                prev0=i
                prev1=None
        return res-1 if res >=1 else res + 1