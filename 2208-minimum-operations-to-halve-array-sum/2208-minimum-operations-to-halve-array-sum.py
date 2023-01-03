class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        pq = []
        for n in nums:
            heapq.heappush(pq, -n)
        curr = total
        l = 0
        while total / 2 < curr:
            val = -heapq.heappop(pq)
            half = val / 2
            curr  = curr - val + half
            heapq.heappush(pq, -half)
            l += 1
        return l