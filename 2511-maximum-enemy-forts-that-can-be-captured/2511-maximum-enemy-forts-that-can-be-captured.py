class Solution:
    def captureForts(self, forts: List[int]) -> int:
        res   = -1
        prev1 = -1
        prev0 = -1
        for i,v in enumerate(forts):
            if v == 1:
                if prev0 >= 0:
                    res = max(res, abs(prev0-i))
                prev0 = -1
                prev1 = i
            elif v == -1:
                if prev1 >= 0:
                    res = max(res, abs(prev1-i))
                prev0 =i
                prev1 =-1
        return res-1 if res >=1 else res + 1