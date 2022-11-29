class Solution:
    def reachNumber(self, target: int) -> int:
        curr = 0
        i = 0
        target = abs(target)
        while True :
            curr += i
            if curr == target or( curr > target and (curr-target) % 2 == 0):
                return i
            i += 1