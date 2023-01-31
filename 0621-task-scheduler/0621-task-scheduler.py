class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        count=Counter(tasks)
        res = 0
        q = deque()
        pq = [(-v,c) for c,v in count.items()]
        heapify(pq)
        while pq:
            while pq and ( len(q) <= n ):
                v,c = heappop(pq)
                v = -v
                q.append((v-1,c))
            curr = len(q)
            while len(q):
                v,c = q.popleft()
                if v > 0:
                    heappush(pq,(-v,c))
            if pq:
                res += ((n - curr) + 1 if curr <= n else 0 )

        return res + len(tasks)