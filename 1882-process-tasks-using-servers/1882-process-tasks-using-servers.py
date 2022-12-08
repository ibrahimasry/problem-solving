class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        idle = []
        running = []
        ans = [-1] * len(tasks)
        for i  , w in enumerate(servers):
            heapq.heappush(idle, (w, i))
        for start,  t in enumerate(tasks):
            while running and running[0][0] <= start:
                endTime, w, i = heapq.heappop(running)
                heapq.heappush(idle, (w, i))
            if idle:
                w, j  = heapq.heappop(idle)
                ans[start] = j
                heapq.heappush(running, (t + start, servers[j], j))
            else :
                endSession , w, k = heapq.heappop(running)
                ans[start] = k
                heapq.heappush(running, (endSession + t, servers[k], k))
        return ans