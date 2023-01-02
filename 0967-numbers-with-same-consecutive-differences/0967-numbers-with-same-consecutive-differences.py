class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        q = deque(list(range(1,10)))
        while n > 1:
            for _ in range(len(q)):
                curr = q.popleft()
                r = curr % 10
                if r + k < 10:
                    q.append(curr * 10 + (r + k))
                if r - k >= 0:
                    q.append(curr * 10 + (r - k))
            n -= 1
        return set(q)