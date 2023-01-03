class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special = [bottom-1] + special + [top+1]
        special.sort()
        res = 0
        for r,c in zip(special[:], special[1:]):
            res = max(res, c-r-1)
        return res