class Solution:
    def getLucky(self, ss: str, k: int) -> int:
        
        s = 0
        
        for c in ss:
            code = (ord(c) - ord("a")) + 1
            s += code % 10
            s += code // 10
        curr = 0
        k-=1
        while k:
            curr += (s % 10)
            s //= 10
            if s == 0:
                s = curr
                curr = 0
                k -= 1
        return s