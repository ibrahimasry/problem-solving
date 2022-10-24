class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        curr = startFuel
        pq = []
        i = 0
        n = len(stations)
        ans = 0
        while curr < target:
            while i < n and curr >= stations[i][0]:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq:
                return -1

            curr += -heapq.heappop(pq)
            ans += 1



        return ans