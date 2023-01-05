class Solution:
    def appealSum(self, s: str) -> int:
        res = 0
        last = {}
        for i, c in enumerate(s):
            last[c] = i + 1
            res +=  sum(last.values())
        return res