class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        
        res = 2
        first = intervals[0][1]-1
        second = intervals[0][1]
        for curr in intervals[1:]:
            if curr[0] > second:
                res += 2
                first = curr[1] -1
                second = curr[1]
            elif curr[0] > first :
                res += 1
                first = curr[1] - 1 if second == curr[1] else second
                second = curr[1]
        return res