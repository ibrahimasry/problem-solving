class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        prefix = [0] + list(accumulate(stations))
        def can(t):
            count = 0
            n = len(stations)
            sweep = [0] * n
            added = 0
            for i in range(n):
                prev = 0
                added -= sweep[i]
                total = (prefix[min(i+r+1,n)] - prefix[max(0, i-r)])  + added
                if t > total:
                    req = t - total
                    added += req
                    count += req
                    if count > k: return False
                    if (i + r*2 + 1) < n:
                        sweep[i+r*2+1] = req
            return True
        h = 10**20
        l = 0
        
        while l < h:
            m = (l+h+1) >> 1
            if can(m):
                l = m
            else:
                h = m-1
        return l