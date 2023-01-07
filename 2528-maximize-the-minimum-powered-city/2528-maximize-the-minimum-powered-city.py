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
                mn = i - r
                if i - r < 0:
                    mn = 0
                mx = i + r
                if mx >= n:
                    mx = n-1
                total = (prefix[mx+1] - prefix[mn])  + added
                if t > total:
                    req = t - total
                    added += req
                    count += req
                    if count > k:
                        return False
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