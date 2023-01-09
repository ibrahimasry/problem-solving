class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        pos = sum([num for num in nums if num > 0])
        if k == 1: return pos
        nums = [abs(num) for num in nums]
        nums.sort()
        pq = [[nums[0],0]]
        for _ in range(3,k+1):
            s , i = heapq.heappop(pq)
            if i < len(nums) -1:
                heapq.heappush(pq, [s + nums[i+1],i+1 ])
                heapq.heappush(pq, [s - nums[i] + nums[i+1], i+1 ])
        return pos - pq[0][0]
        