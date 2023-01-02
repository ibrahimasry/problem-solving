class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
        events = []
        for s,e in intervals:
            events.append([s,1])
            events.append([e+1,-1])
        events.sort()
        
        res = 0
        running = 0
        
        for _, dir in events:
            running += dir
            res = max(running, res)
        return res