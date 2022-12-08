class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [-x for x in piles]
        heapq.heapify(pq)
        
        while k :
            curr = -heapq.heappop(pq)
            k -= 1
            if ceil(curr/ 2) > 0:
                heapq.heappush(pq,-ceil(curr/2))
        return -sum(pq)