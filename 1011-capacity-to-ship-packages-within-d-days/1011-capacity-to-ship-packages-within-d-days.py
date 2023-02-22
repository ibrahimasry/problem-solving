class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def good(m):
            curr = m
            k = 0
            for n in weights:
                if curr < n:
                    curr = m
                    k += 1
                curr -= n
            return k + 1 <= days
        l = max(weights)
        r = sum(weights)+1
        
        while l < r:
            m = (l+r)>>1
            if good(m):
                r = m
            else:
                l = m + 1
        return l