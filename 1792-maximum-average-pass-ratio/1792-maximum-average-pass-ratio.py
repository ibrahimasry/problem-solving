class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
        
        for x, y in classes:
            heapq.heappush(pq, (x/y - (x+1)/(y+1), x, y))
        while extraStudents:
            _ , x, y = heapq.heappop(pq)
            x += 1
            y += 1
            heapq.heappush(pq, (x/y - (x+1)/(y+1), x, y))
            extraStudents -= 1
        return sum([x/y for _ , x, y in pq]) / len(classes)