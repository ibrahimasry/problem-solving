class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if sum(arr) <= target:
            return max(arr)
        def good(m):
            curr = sum(arr)
            for n in arr:
                if n > m:
                    curr = (curr - n) + m
            return curr 
        
        l = 0
        r = 10 ** 10
        res = inf
        num = -1
        while l < r:
            m = (l+r) >> 1
            curr = good(m)
            if (curr - target) >= 0:
                r = m 
            else :
                l = m + 1
        s1 = 0
        s2 = 0
        for n in arr:
            if n > l:
                s1 += l
            else :
                s1 += n
            if n > l - 1:
                s2 += l - 1
            else:
                s2 += n
        return l if abs(s1-target) < abs(s2-target) else l - 1