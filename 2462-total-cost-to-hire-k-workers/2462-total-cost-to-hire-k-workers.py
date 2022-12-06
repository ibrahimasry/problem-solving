class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        seen = set()
        
        n = len(costs)
        pq = []
        for i in range(min(candidates, n)):
                heapq.heappush(pq, (costs[i], -1))
                seen.add(i)
        for i in range(max(candidates, n-candidates), n):
                heapq.heappush(pq, (costs[i], 1))
        ans  = 0
        maxLeft = candidates - 1
        minRight = n - candidates
        while k :
            cost,  i = heapq.heappop(pq)
            ans += cost
            k -= 1
            if( maxLeft + 1 >= minRight) :
                continue
            if i == 1:
                heapq.heappush(pq, (costs[minRight-1],1))
                minRight -= 1
            else :
                heapq.heappush(pq, (costs[maxLeft+1], -1))
                maxLeft += 1
        return ans