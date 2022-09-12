class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        
        
                
        events = []
        
        for i, s in enumerate(startTime) :
            events.append((s, 1 , endTime[i] , profit[i]))
            
            
        res = 0
        heapq.heapify(events)
        while len(events):
            s, time, e , p = heapq.heappop(events)
            
            if time == 1 :
                heapq.heappush(events, (e , -1 , s , p + res))
            else :
                res = max(res, p)
                
        return res         
        