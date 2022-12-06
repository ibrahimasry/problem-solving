class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        seen = set()
        
        n = len(costs)
        pq = []
        for i in range(min(candidates, n)):
                heapq.heappush(pq, (costs[i],i, -1))
                seen.add(i)
        for i in range(max(candidates, n-candidates), n):
                heapq.heappush(pq, (costs[i], i,1))
        ans  = 0
        maxLeft = candidates 
        minRight = n - candidates - 1
        while k :
            cost, index, i = heapq.heappop(pq)
            ans += cost
            k -= 1
            if maxLeft > minRight:
                continue
            if i == 1:
                heapq.heappush(pq, (costs[minRight], minRight,1))
                minRight -= 1
            else :
                heapq.heappush(pq, (costs[maxLeft], maxLeft, -1))
                maxLeft += 1
        return ans