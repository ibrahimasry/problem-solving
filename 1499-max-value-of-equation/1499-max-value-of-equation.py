class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = deque()
        res = -inf
        for x, y in points:
            while q and x - q[0][1] > k:
                q.popleft()
            if q:
                res = max(res, q[0][0] + x + y)
            while q and q[-1][0] < y - x:
                q.pop()
            q.append((y-x,x))
        return res