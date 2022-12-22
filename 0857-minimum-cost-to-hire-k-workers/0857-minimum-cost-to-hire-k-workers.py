class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([[float(w)/q,q] for w,q in zip(wage,quality)])
        res = inf
        qsum = 0
        pq = []
        for r, q in workers:
            qsum += q
            heapq.heappush(pq,-q)
            if len(pq) > k:
                qsum += heapq.heappop(pq)
            if len(pq) == k:
                res = min(res, r * qsum)
        return res