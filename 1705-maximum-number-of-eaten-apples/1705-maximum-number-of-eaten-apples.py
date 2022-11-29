class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        
        
        
        pq = []
        
        day = 0
        i = 0
        n = len(apples)
        while i < n or pq:
            if i < n and apples[i]:
                heapq.heappush(pq, [days[i]+i, apples[i]])
            
            while pq and (pq[0][0] <= i):
                heapq.heappop(pq)
            if pq:
                pq[0][1] -= 1
                day += 1
                if pq[0][1] == 0:
                    heapq.heappop(pq)

            i += 1
        return day
                