class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def good(c,m,k):
            count = 0
            curr = 0
            
            for d in bloomDay:
                if d <= c :
                    curr += 1
                    if curr == k:
                        curr = 0
                        count += 1
                elif d > c:
                    curr = 0
            return count >= m
        
        l = 1
        r = max(bloomDay) + 1
        while l < r:
            mid = (l+r) >> 1
            if good(mid, m, k):
                r = mid
            else :
                l = mid + 1
        return l if l <= max(bloomDay) else -1