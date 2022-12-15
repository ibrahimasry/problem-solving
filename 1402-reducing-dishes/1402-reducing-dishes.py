class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        total = 0
        res = 0
        for n in satisfaction[::-1]:
            if total + n  > 0:
                total += n
                res += total 
        return res