class Solution:
    def maxNumberOfFamilies(self, n: int, reserved: List[List[int]]) -> int:
        hash = defaultdict(set)
        
        for r , c in reserved:
            if c in [2,3,4,5]:
                hash[r].add(0)
            if c in [4,5,6,7]:
                hash[r].add(1)
            if c in [6,7,8,9]:
                hash[r].add(2)
        res = 2 * n
        for v in hash.values():
            if len(v) == 3:
                res -= 2
            else :
                res -= 1
        return res