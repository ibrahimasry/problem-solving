class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        efficiency = sorted([[v,speed[k]] for k,v in enumerate(efficiency)])
        start = n - 1
        speedSum =  0
        best = 0 
        pq = []
        while start >= 0:
            speedSum += efficiency[start][1]
            heapq.heappush(pq, efficiency[start][1])
            if len(pq) > k:
                speedSum -= heapq.heappop(pq)
            best = max(best, speedSum * efficiency[start][0])

            start -= 1



        return best % (10**9 + 7)
            