class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        invalid = set()
        
        for i , j in zip(fronts, backs):
            if i == j:
                invalid.add(i)
        res = sys.maxsize
        for i, j in zip(fronts, backs):
            if i < res and i not in invalid:
                res = min(i, res)
            if j < res and j not in invalid:
                res = min(j, res)
        return 0 if res == sys.maxsize else res