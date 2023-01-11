class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        pq = []
        a = sorted(zip(capital , profits))
        i = 0
        while  k:
            while i < len(profits) and a[i][0] <= w:
                heapq.heappush(pq,-a[i][1])
                i += 1
            if pq:
                w -= heapq.heappop(pq)
            k -= 1
        return w