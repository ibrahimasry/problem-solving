class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = 0
        
        prev = 0
        
        for n in arr:
            diff = ((n-prev) -1) if n - prev > 1 else 0
            if k - diff <= 0:
                return prev + k
            k -= diff
            prev = n 
        return prev + k