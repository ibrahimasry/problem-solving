class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        
        tasks = [[s,e,i] for i, (s,e) in enumerate(tasks)]
        tasks.sort()
        time = tasks[0][0]
        pq = []
        i = 0
        ans = []
        while i < len(tasks) or pq :
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(pq, (tasks[i][1], tasks[i][2],i))
                i += 1
            if i < len(tasks) and not pq:
                time = tasks[i][0]
            if pq:
                t , k,j = heapq.heappop(pq)
                time += t
                ans.append(k)
        return ans