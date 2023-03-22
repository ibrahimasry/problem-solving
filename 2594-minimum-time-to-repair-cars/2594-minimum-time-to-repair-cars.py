class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        
        l = 0
        h = 10**20
        while l < h:
            m = l + h >> 1
            s = 0
            for r in ranks:
                s += int(sqrt((m/r)))
            if s >= cars:
                h = m
            else:
                l = m + 1
        return l
            