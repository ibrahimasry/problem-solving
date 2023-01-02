class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = Counter()
        for s,e in intervals:
            events[s] += 1
            events[e+1] -= 1
        
        res = 0
        running = 0
        
        for _, dir in sorted(events.items()):
            running += dir
            res = max(running, res)
        return res