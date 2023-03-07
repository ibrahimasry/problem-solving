class Solution:
    def minimumTime(self, times: List[int], totalTrips: int) -> int:
        times.sort(reverse=True)
        
        def good(t):
            res = 0
            for time in times:
                res += t // time
            return res >= totalTrips
        
        l = 0
        h = times[0] * totalTrips + 1
        while l < h:
            m = l + h >> 1
            if good(m):
              h = m
            else :
                l = m + 1
        return l