class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        pq = [abs(nums1[i]-nums2[i]) * -1  for i in range(len(nums1))]
        if k1 + k2 > -sum(pq):
            return 0

        summ = k1 + k2
        heapq.heapify(pq)
        while summ > 0 and pq:
            curr = -heapq.heappop(pq)
            gap = max(summ // len(nums1), 1)
            curr -= gap
            if curr > 0:
                heapq.heappush(pq, -curr)
            summ -= gap
        return sum([pq[i]**2 for i in range(len(pq))])