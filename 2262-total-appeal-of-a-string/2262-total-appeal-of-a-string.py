class Solution:
    def appealSum(self, s: str) -> int:
        res = 0
        last = {}
        for i, c in enumerate(s):
            last[c] = i
            res += len(last) + sum(last.values())
        return res