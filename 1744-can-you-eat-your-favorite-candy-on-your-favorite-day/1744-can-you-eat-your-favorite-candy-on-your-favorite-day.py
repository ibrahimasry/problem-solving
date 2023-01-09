class Solution:
    def canEat(self, candiesCount: List[int], q: List[List[int]]) -> List[bool]:
        prefix = [0] + list(accumulate(candiesCount))
        ans = []
        for f,d,c in q:
            if d >= prefix[f+1] or c * (d+1) - 1 < prefix[f] :
                ans.append(False)
            else:
                ans.append(True)
        return ans