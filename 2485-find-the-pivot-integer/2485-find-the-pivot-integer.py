class Solution:
    def pivotInteger(self, n: int) -> int:
        
        total = n * (n+1) // 2
        
        p = int(sqrt(total))
        if p * p == total:
            return p
        return -1