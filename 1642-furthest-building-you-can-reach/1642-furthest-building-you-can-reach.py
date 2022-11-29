class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        pq = []
        
        total = 0
        
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            
            if diff <= 0 :
                continue
            total += diff
            heapq.heappush(pq, -diff)
            if total > bricks:
                if ladders == 0:
                    return i
                ladders -= 1
                total += heapq.heappop(pq)
        return n-1