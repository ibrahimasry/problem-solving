class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        
        intervals.sort()
        queries = [[q, i]  for i, q in enumerate(queries)]
        queries.sort()
        
        pq = []
        
        ans = [-1] * len(queries)
        
        j = 0
        n = len(intervals)
        for num , i in queries:
            
            while j < n and intervals[j][0] <= num:
                if intervals[j][1] >= num:
                    l , r = intervals[j]
                    heapq.heappush(pq, [r - l + 1, r])
                j += 1
            while pq and pq[0][1] < num:
                heapq.heappop(pq)
            if len(pq):   
                ans[i] = pq[0][0]
        return ans   
            