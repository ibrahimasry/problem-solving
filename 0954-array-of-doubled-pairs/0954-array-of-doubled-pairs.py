class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        
        for n in sorted(arr, key=abs):
            if count[n] == 0:
                continue
            if count[2*n] == 0:
                return False
            count[n] -= 1
            count[2*n] -= 1
        return True