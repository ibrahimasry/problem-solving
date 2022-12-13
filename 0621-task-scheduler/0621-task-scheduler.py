class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        pq = []
        
        for k, v in freq.items():
            heapq.heappush(pq, -v)
            
        res = 0
        prev = []
        while pq:
            
            prev = []
            count = -1
            while pq and count < n:
                prev.append(heapq.heappop(pq))
                prev[-1] += 1
                res += 1
                count += 1
            prevLen = len(prev) - 1
            for v in prev:
                if v < 0:
                    heapq.heappush(pq, v)
            if prevLen < n  and pq:
                res += n-prevLen


        return res