class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        
        
        events = []
        
        for s, e , t in rides :
            events.append((s, 1,  t , e))
            
            
        res = 0
        heapq.heapify(events)
        while len(events):
            s, time, earning , e= heapq.heappop(events)
            
            if time == 1 :
                heapq.heappush(events, (e , -1 , res + (e-s+earning), s))
            else :
                res = max(res, earning)
                
        return res         