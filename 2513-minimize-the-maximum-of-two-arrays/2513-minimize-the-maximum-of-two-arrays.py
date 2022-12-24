class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def good(target):
            m1 = target - (target // divisor1)
            m2 = target - (target // divisor2)
            m3 = target - (target // lcm(divisor1, divisor2))
            if uniqueCnt1 + uniqueCnt2 <= m3 and m1 >= uniqueCnt1 and m2 >= uniqueCnt2:
                return True
            return False
        l = 2
        r = 10 ** 15
        
        while l < r:
            m = (l+r) >> 1
            if good(m):
                r = m
            else :
                l = m + 1
        return l