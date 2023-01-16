class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]
        
        i = 0
        
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1
        res = intervals[:i]
        
        prev = newInterval
        for s,e in intervals[i:]:
            if s <= prev[1]:
                prev[0] = min(s,prev[0])
                prev[1] = max(e,prev[1])
            else:
                res.append(prev)
                prev = [s,e]
        res.append(prev)
        return res