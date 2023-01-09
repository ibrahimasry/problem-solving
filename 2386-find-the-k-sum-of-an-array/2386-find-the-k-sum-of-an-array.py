class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        pos = sum([num for num in nums if num > 0])
        nums = [abs(num) for num in nums]
        nums.sort()
        pq = [[nums[0],0]]
        if k == 1:
            return pos
        while k>2:
            s , i = heapq.heappop(pq)
            if i < len(nums) -1:
                heapq.heappush(pq, [s + nums[i+1],i+1 ])
                heapq.heappush(pq, [(s - nums[i]) + nums[i+1], i+1 ])
            k -= 1
        if not pq:
            return pos
        return pos - pq[0][0]
        