class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        
        events.sort()
        pq = []
        days = 1
        res = 0
        maxDay = max([e for s, e in events])
        i = 0
        n = len(events)
        while days <= maxDay:
            while i < n and events[i][0] <= days:
                heapq.heappush(pq, events[i][1])
                i += 1
            while pq and pq[0] < days:
                heapq.heappop(pq)
            if pq:
                res += 1
                heapq.heappop(pq)
            days += 1
        return res
            
        