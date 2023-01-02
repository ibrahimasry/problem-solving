class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        res= 0
        for c in s:
            if c in seen:
                seen = set()
                res += 1
            seen.add(c)
            
        if len(seen):
            res += 1
        return res
