class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        count = Counter(arr)
        n = len(count)
        for v in sorted(count.values()):
            if v - k <= 0:
                k -= v
                n -= 1
            else:
                return n
        return n